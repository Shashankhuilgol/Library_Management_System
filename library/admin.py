from django.contrib import admin
from library.models import Author, Book, Borrower, BorrowedBook

# Register your models here.

admin.site.register(Author)
admin.site.register(Book)
admin.site.register(Borrower)
admin.site.register(BorrowedBook)

