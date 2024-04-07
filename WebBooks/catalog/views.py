from django.http import HttpResponseRedirect, HttpResponseNotFound
from django.shortcuts import render
from .models import Book, Author, BookInstance, Genre
from .forms import Form_add_author, Form_edit_author
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from django.urls import reverse, reverse_lazy


class AuthorDetailView(DetailView):
    model = Author
    # context_object_name = 'author'


class AuthorListView(ListView):
    model = Author
    # context_object_name = 'authors'
    paginate_by = 3


class BookDeatilView(DetailView):
    model = Book
    context_object_name = 'book'


class BookListView(ListView):
    model = Book
    context_object_name = 'books'
    paginate_by = 3


def about(request):
    text_head = 'Сведения о компании'
    name = 'Компания "Мир Книг"'
    rab1 = 'Наш каталог книг постоянно обновляется, предлагая Вам последние новинки и проверенные временем шедевры.'
    rab2 = 'Мы сами являемся страстными читателями и отбираем лучшие издания, чтобы поделиться ими с вами.'
    rab3 = 'Заказывайте книги в несколько кликов и получайте их в кратчайшие сроки, благодаря нашей быстрой доставке.'
    rab4 = 'Мы организовываем встречи с популярными авторами и молодыми талантами, давая вам возможность погрузиться в творческий процесс.'
    context = {'text_head': text_head, 'name': name, 'rab1': rab1, 'rab2': rab2, 'rab3': rab3, 'rab4': rab4}
    # передача словаря context с данными в шаблон
    return render(request, 'catalog/about.html', context)


def contact(request):
    text_head = 'Контакты'
    name = 'Компания "Мир Книг"'
    address = 'Москва, Сивцев Вражек, 27'
    tel = '8-800-555-35-35'
    email = 'MirKnig@example.com'
    # Словарь для передачи данных в шаблон index.html
    context = {'text_head': text_head, 'name': name, 'address': address, 'tel': tel, 'email': email}
    # передача словаря context с данными в шаблон
    return render(request, 'catalog/contact.html', context)


def index(request):
    text_head = "На нашем сайте вы можете получить книги в электронном виде"
    # Данные о книгах и их количестве
    books = Book.objects.all()
    num_books = Book.objects.all().count()
    # Данные об экземплярах книг в БД
    num_instances = BookInstance.objects.all().count()
    # Доступные книги (статус = 'На складе')
    num_instances_available = BookInstance.objects.filter(status__exact=2).count()
    # Данные об авторах книг
    author = Author.objects
    num_authors = Author.objects.count()
    # Число посещенйи этого view, подсчитывает в переменной session
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1
    # Словарь для передачи данных в шаблон index.html
    context = {
        'text_head': text_head,
        'books': books,
        'num_books': num_books,
        'num_instances': num_instances,
        'num_instances_available': num_instances_available,
        'author': author,
        'num_authors': num_authors,
        'num_visits': num_visits,
    }
    # Передача словаря context с данными в шаблон
    return render(request, 'catalog/index.html', context)


def logged_out(request):
    # Логика для отображения страницы после выхода из системы
    return render(request, 'registration/logged_out.html')


class LoanedBooksByUserListView(LoginRequiredMixin, generic.ListView):
    # Универсальный класс представления списка книг,
    # находящийся в заказе у текущего пользователя
    model = BookInstance
    template_name = 'catalog/bookinstance_list_borrowed_user.html'
    paginate_by = 10

    def get_queryset(self):
        return BookInstance.objects.filter(borrower=self.request.user).filter(status__exact='2').order_by('due_back')


# Вызов страницы для редактирования автора
def edit_authors(request):
    author = Author.objects.all()
    context = {'author': author}
    return render(request, "catalog/edit_authors.html", context)


# Создание нового автора в БД
def add_author(request):
    if request.method == 'POST':
        form = Form_add_author(request.POST, request.FILES)
        if form.is_valid():
            # Получить данные из формы
            first_name = form.cleaned_data.get('first_name')
            last_name = form.cleaned_data.get('last_name')
            date_of_birth = form.cleaned_data.get('date_of_birth')
            about = form.cleaned_data.get('about')
            photo = form.cleaned_data.get('photo')
            # Создание объекта для записи в БД
            obj = Author.objects.create(first_name=first_name, last_name=last_name, date_of_birth=date_of_birth,
                                        about=about, photo=photo)
            # Сохранить полученные данные
            obj.save()
            # Загрузить страницу со списком авторов
            return HttpResponseRedirect(reverse('authors-list'))
    else:
        form = Form_add_author()
        context = {'form': form}
        return render(request, "catalog/authors_add.html", context)


# Удаление автора из БД
def delete(request, id):
    try:
        author = Author.objects.get(id=id)
        author.delete()
        return HttpResponseRedirect("/edit_authors/")
    except:
        return HttpResponseNotFound("<h2>Автор не найден</h2>")


# Изменение данных об авторе в БД
def edit_author(request, id):
    author = Author.objects.get(id=id)
    # author = get_object_or_404(Author, id=id)
    if request.method == 'POST':
        instance = Author.objects.get(pk=id)
        form = Form_edit_author(request.POST, request.FILES, instance=instance)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/edit_authors/")
    else:
        form = Form_edit_author(instance=author)
        content = {'form': form}
        return render(request, "catalog/edit_author.html", content)


# Вызов страницы для редактирования книг
def edit_books(request):
    book = Book.objects.all()
    context = {'book': book}
    return render(request, "catalog/edit_books.html", context)


# Класс для создания в БД новой записи о книге
class BookCreate(CreateView):
    model = Book
    fields = '__all__'
    success_url = reverse_lazy('edit_books')


# Класс дял обновления в БД записи о книге
class BookUpdate(UpdateView):
    model = Book
    fields = '__all__'
    success_url = reverse_lazy('edit_books')


# Класс для удаления из БД записи о книге
class BookDelete(DeleteView):
    model = Book
    success_url = reverse_lazy('edit_books')
