from django.contrib import admin

from .models import Book, BookGenre, BookImage

# Register your models here.
class BookAdmin(admin.ModelAdmin):
    list_display = ['ISBN_number', 'title', 'author', 'page_count', 'publish_date']
    search_field = ['ISBN_number', 'title', 'author', 'publish_date']
    list_filter = ['ISBN_number', 'title', 'author', 'publish_date']

    class Meta:
        model = Book

class BookGenreAdmin(admin.ModelAdmin):
    list_display = ['book', 'genre']

class BookImageAdmin(admin.ModelAdmin):
    list_display = ['book', 'image']

admin.site.register(Book, BookAdmin)
admin.site.register(BookGenre, BookGenreAdmin)
admin.site.register(BookImage, BookImageAdmin)
