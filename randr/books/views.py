from django.shortcuts import get_object_or_404, render, redirect
from .models import Book, PublishHouse, Author
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from .choices import Category_Choice
from cart.forms import CartAddProductForm


def index(request):
    books = Book.objects.all()
    paginator = Paginator(books, 8)
    page = request.GET.get('page')
    paged_book = paginator.get_page(page)

    context = {
        'books': paged_book
    }

    return render(request, 'books/books.html', context)


def book(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    similar_books = Book.objects.all().exclude(pk=book_id).order_by('?')[:4]
    cart_product_form = CartAddProductForm()

    book_context = {
        'book': book,
        'similar_books': similar_books,
        'cart_product_form': cart_product_form
    }
    return render(request, 'books/book.html', book_context)


def advanced_search(request):
    publish_houses = PublishHouse.objects.all()
    authors = Author.objects.all()

    context = {
        'publish_houses': publish_houses,
        'authors': authors,
        'Category_Choice': Category_Choice,

    }

    return render(request, 'books/advanced_search.html', context)


def result(request):
    publish_houses = PublishHouse.objects.all()
    authors = Author.objects.all()
    queryset_list = Book.objects.order_by('-book_date')

    # Title
    if 'title' in request.GET:
        title = request.GET['title']
        if title:
            queryset_list = queryset_list.filter(title__icontains=title)

    # Author
    if 'author' in request.GET:
        author = request.GET['author']
        if author:
            queryset_list = queryset_list.filter(author__name__iexact=author)

    # Category
    if 'category' in request.GET:
        category = request.GET['category']
        if category:
            queryset_list = queryset_list.filter(classification__iexact=category)

    # Publish house
    if 'publisher' in request.GET:
        publisher = request.GET['publisher']
        if publisher:
            queryset_list = queryset_list.filter(publish_house__name__iexact=publisher)

    # Price
    if 'min_price' and 'max_price' in request.GET:
        min_price = request.GET['min_price']
        max_price = request.GET['max_price']
        if min_price and max_price:
            queryset_list = queryset_list.filter(price__gte=min_price, price__lte=max_price)

    context = {
        'publish_houses': publish_houses,
        'authors': authors,
        'Category_Choice': Category_Choice,
        'books': queryset_list,
        'values': request.GET,
    }

    return render(request, 'books/result.html', context)




