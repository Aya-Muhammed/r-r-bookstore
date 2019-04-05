from django.shortcuts import get_object_or_404, render
from .models import Accessory
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator


def index(request):
    accessories = Accessory.objects.all()
    paginator = Paginator(accessories, 6)
    page = request.GET.get('page')
    paged_accessory = paginator.get_page(page)

    context = {
        'accessories': paged_accessory
    }
    return render(request, 'accessories/accessories.html', context)


def accessory(request, accessory_id):
    accessory = get_object_or_404(Accessory, pk=accessory_id)

    accessory_context = {
        'accessory': accessory
    }

    return render(request, 'accessories/accessory.html', accessory_context)
