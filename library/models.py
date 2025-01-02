from django.db import models

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=50)
    bio = models.TextField(blank=True)

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=50)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    available = models.BooleanField(default=True)

    def __str__(self):
        return self.title

class Borrower(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.name

class BorrowedBook(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    borrower = models.ForeignKey(Borrower, on_delete=models.CASCADE)
    borrowed_date = models.DateField(auto_now_add=True)
    return_date = models.DateField(null=True, blank=True)
