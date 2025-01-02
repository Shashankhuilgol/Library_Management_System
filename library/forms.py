from django import forms
from .models import BorrowedBook

class BorrowedBookForm(forms.ModelForm):
    class Meta:
        model = BorrowedBook
        fields = ['book', 'borrower', 'return_date']
