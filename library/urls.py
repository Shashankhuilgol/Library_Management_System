from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('books/', views.book_list, name='book_list'),
    path('borrow/<int:book_id>/', views.borrow_book, name='borrow_book'),
    path('borrowed/', views.borrowed_books_list, name='borrowed_books_list'), 
    path('return/<int:borrowed_id>/', views.return_book, name='return_book'),
]
