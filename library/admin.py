from django.contrib import admin
from library.models import Author, Book, Borrower, BorrowedBook

# Register your models here.

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'category', 'available')


admin.site.register(Author)
admin.site.register(Book,BookAdmin)
admin.site.register(Borrower)
admin.site.register(BorrowedBook)

