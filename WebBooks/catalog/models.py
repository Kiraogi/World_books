from django.db import models
from django.urls import reverse


# Жанр книг
class Genre(models.Model):
    name = models.CharField(max_length=200, help_text="Введите жанр книги", verbose_name="Жанр книги")

    def __str__(self):
        return self.name


# Язык книг
class Language(models.Model):
    name = models.CharField(max_length=20, help_text="Введите язык книги", verbose_name="Язык книги")

    def __str__(self):
        return self.name


# Издательство
class Publisher(models.Model):
    name = models.CharField(max_length=20, help_text="Введите наименование издательства", verbose_name="Издательство")

    def __str__(self):
        return self.name


# Автор
class Author(models.Model):
    first_name = models.CharField(max_length=100, help_text="Введите имя автора", verbose_name="Имя автора")
    last_name = models.CharField(max_length=100, help_text="Введите фамилию автора", verbose_name="Фамилия автора")
    date_of_birth = models.DateField(help_text="Введите дату рождения", verbose_name="Дата рождения", null=True,
                                     blank=True)
    about = models.TextField(help_text="Введите сведения об авторе", verbose_name="Сведения об авторе")
    photo = models.ImageField(upload_to="images", help_text="Введите фото автора", verbose_name="Фото автора",
                              null=True, blank=True)

    def __str__(self):
        return self.last_name


# Книга
class Book(models.Model):
    title = models.CharField(max_length=200, help_text="Введите название книги", verbose_name="Название книги")
    genre = models.ForeignKey('Genre', on_delete=models.CASCADE, help_text="Выберите жанр для книги",
                              verbose_name="Жанр книги", null=True)
    language = models.ForeignKey('Language', on_delete=models.CASCADE, help_text="Выберите язык для книги",
                                 verbose_name="Язык книги", null=True)
    publisher = models.ForeignKey('Publisher', on_delete=models.CASCADE, help_text="Выберите издательство для книги",
                                  verbose_name="Издательство", null=True)
    year = models.CharField(max_length=4, help_text="Введите год издания книги", verbose_name="Год издания книги")
    author = models.ManyToManyField('Author', help_text="Выберите автора (авторов) для книги",
                                    verbose_name="Автор (авторы) книги")
    summary = models.TextField(max_length=1000, help_text="Введите краткое описание книги",
                               verbose_name="Аннотация книги")
    isbn = models.CharField(max_length=20, help_text="Введите ISBN книги (до 20  символов)", verbose_name="ISBN книги")
    price = models.DecimalField(max_digits=7, decimal_places=2, help_text="Введите цену книги",
                                verbose_name="Цена книги (руб.)")
    photo = models.ImageField(upload_to="images", help_text="Введите изображение обложки",
                              verbose_name="Изображение обложки")

    # Функция формирования списка авторов
    def display_author(self):
        return ', '.join([author.last_name for author in self.author.all()])

    display_author.short_description = "Автор(ы)"

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('book-detail', args=[str(self.id)])


# Состояние экземпляра книги
class Status(models.Model):
    name = models.CharField(max_length=20, help_text="Введите статус экземпляра книги",
                            verbose_name="Статус экземпляра книги")

    def __str__(self):
        return self.name


# Экземпляр книги
class BookInstance(models.Model):
    book = models.ForeignKey('Book', on_delete=models.CASCADE, null=True)
    inv_nom = models.CharField(max_length=20, help_text="Введите инвентарный номер экземпляра книги",
                               verbose_name="Инвентарный номер", null=True)
    status = models.ForeignKey('Status', on_delete=models.CASCADE, help_text="Изменить состояние экземпляра книги",
                               verbose_name="Статус экземпляра книги")
    due_back = models.DateField(help_text="Введите конец срока статуса", verbose_name="Дата окончания статуса",
                                null=True, blank=True)

    # Метаданные
    class Meta:
        ordering = ['due_back']

    def __str__(self):
        return '%s %s %s' % (self.inv_nom, self.book, self.status)
