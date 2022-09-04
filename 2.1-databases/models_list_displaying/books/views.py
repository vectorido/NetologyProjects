from django.shortcuts import render, redirect
from .models import Book

from datetime import datetime

def index(request):
    return redirect('books')


def books_view(request):
    template = 'books/books_list.html'
    books = Book.objects.all().order_by('pub_date')
    context = {
        'books': books
    }
    return render(request, template, context)


def get_specific_book(request, dt):
    template = 'books/specific_book.html'
    book = Book.objects.get(pub_date=dt)
    prev_date = Book.objects.filter(pub_date__lt=dt).values('pub_date').order_by('pub_date').last()
    next_date = Book.objects.filter(pub_date__gt=dt).values('pub_date').order_by('pub_date').first()
    prev, next = None, None

    if prev_date:
        prev = prev_date.get('pub_date')
    if next_date:
        next = next_date.get('pub_date')
    context = {
        'book': book,
        'prev': prev,
        'next': next,
    }
    return render(request, template, context)