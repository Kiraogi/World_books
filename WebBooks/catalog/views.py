from django.shortcuts import render
from .models import Book, Author, BookInstance, Genre
from django.views.generic import ListView, DetailView


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
    rab1 = 'Продажа книжек'
    rab2 = 'Покупка книжек'
    rab3 = 'Доставка книжек'
    rad4 = 'Оплата книжек'
    context = {'text_head': text_head, 'name': name, 'rab1': rab1, 'rab2': rab2, 'rab3': rab3, 'rad4': rad4}
    # передача словаря context с данными в шаблон
    return render(request, 'catalog/about.html', context)


def contact(request):
    text_head = 'Контакты'
    name = 'Компания "Мир Книг"'
    address = 'Москва, ул. Ленина, д. 1'
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
    # Словарь для передачи данных в шаблон index.html
    context = {
        'text_head': text_head,
        'books': books,
        'num_books': num_books,
        'num_instances': num_instances,
        'num_instances_available': num_instances_available,
        'author': author,
        'num_authors': num_authors
    }
    # Передача словаря context с данными в шаблон
    return render(request, 'catalog/index.html', context)
