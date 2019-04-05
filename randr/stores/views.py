from django.shortcuts import render
from .models import Store
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator


def index(request):
    stores = Store.objects.all()
    paginator = Paginator(stores, 2)
    page = request.GET.get('page')
    paged_store = paginator.get_page(page)

    context = {
        'stores': paged_store
    }
    return render(request, 'stores/stores.html', context)


