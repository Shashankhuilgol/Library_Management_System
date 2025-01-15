from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from django.contrib import messages
from .models import Author, Book, Borrower, BorrowedBook
from .forms import BorrowedBookForm
from library.models import Book
from django.db.models import Q

def home(request):
    return render(request, 'library/home.html')

def index(request):
    query = request.GET.get('q', '')  # Retrieve the search query from the GET request
    books = Book.objects.filter(
        Q(title__icontains=query) |  Q(author__name__icontains=query)  
    )
    return render(request, 'library/index.html', {'books': books, 'query': query})


def book_list(request):
    books = Book.objects.all()
    return render(request, 'library/book_list.html', {'books': books})


def borrow_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)

    if not book.available:
        return redirect('index')
    
    if request.method == 'POST':
        form = BorrowedBookForm(request.POST)
        if form.is_valid():
            borrow = form.save(commit=False)
            borrow.book = book
            borrow.save()
            book.available = False
            book.save()
            messages.success(request, f'You have successfully borrowed the book: {book.title}')
            return redirect('index')
    
    else:
        form = BorrowedBookForm()

    return render(request, 'library/borrow_book.html', {'form': form, 'book': book})

def borrowed_books_list(request):
    borrowed_books = BorrowedBook.objects.all()
    return render(request, 'library/borrowed_books_list.html', {'borrowed_books': borrowed_books})

def return_book(request, borrowed_id):
    borrowed = get_object_or_404(BorrowedBook, id=borrowed_id)
    borrowed.return_date = timezone.now()
    borrowed.save()
    borrowed.book.available = True
    borrowed.book.save()
    borrowed.delete()
    messages.success(request, 'You have successfully returned the book.')
    return redirect('book_list')
