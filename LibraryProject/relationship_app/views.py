from django.shortcuts import render
from .models import Book
from django.http import HttpResponse

# Function-Based View
def list_books(request):
    books = Book.objects.all()
    return render(request, 'list_books.html', {'books': books})

# Create your views here.
