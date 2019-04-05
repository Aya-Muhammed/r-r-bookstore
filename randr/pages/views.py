from django.shortcuts import render
from .models import Advertise
from books.models import Book


def preindex(request):
    return render(request, 'pages/preindex.html')


def index(request):
    new_books = Book.objects.order_by('-book_date')[:4]
    bestselling_books = Book.objects.all().filter(is_best_selling=True)[:4]
    advertises = Advertise.objects.all()
    index_context = {
        'new_books': new_books,
        'advertises': advertises,
        'bestselling_books': bestselling_books,
    }

    return render(request, 'pages/index.html', index_context)






