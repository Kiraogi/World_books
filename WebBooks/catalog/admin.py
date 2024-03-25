from django.contrib import admin
from .models import Author, Book, Genre, Language, Publisher, Status, BookInstance
from django.utils.safestring import mark_safe
from django.utils.html import format_html


# Определяем класс AuthorAdmin для авторов книг
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'photo', 'show_photo')
    fields = ['last_name', 'first_name', ('date_of_birth', 'photo')]
    readonly_fields = ["show_photo"]

    def show_photo(self, obj):
        return format_html(f'<img src="{obj.photo.url}" style="max-height: 100px;">')

    # Можно и с использованием функции mark_safe()
    # return mark_safe(f'<img src="{obj.photo.url}" style="max-height: 100px;">'
    show_photo.short_description = 'Фото'
    # admin.site.register(Author)


# Регистрируем класс AuthorAdmin для авторов книг
admin.site.register(Author, AuthorAdmin)


# admin.site.register(Book)

class BookInstanceInline(admin.TabularInline):
    model = BookInstance


# Регистрация класса BookAdmin для книг
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'genre', 'language', 'display_author', 'show_photo')
    list_filter = ('author', 'genre', 'language')
    inlines = [BookInstanceInline]
    readonly_fields = ["show_photo"]

    def show_photo(self, obj):
        return format_html(f'<img src="{obj.photo.url}" style="max-height: 100px;">')

    show_photo.short_description = 'Обложка'
    # admin.site.register(BookInstance)


# Регистрация класса BookInstanceAdmin для экземпляров книг
@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    # list_display = ('inv_nom', 'book', 'status', 'due_back')
    # list_filter = ('book', 'status', 'due_back')
    list_filter = ('book', 'status')
    fieldsets = (
        ('Экземпляр книги', {'fields': ('book', 'inv_nom')}),
        ('Статус и окончание его действия', {'fields': ('status', 'due_back')}),
    )


admin.site.register(Genre)
admin.site.register(Language)
admin.site.register(Publisher)
admin.site.register(Status)
