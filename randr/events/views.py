from django.shortcuts import get_object_or_404, render
from .models import Event
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator


def index(request):
    events = Event.objects.all()
    paginator = Paginator(events, 2)
    page = request.GET.get('page')
    paged_event = paginator.get_page(page)

    context = {
        'events': paged_event
    }
    return render(request, 'events/events.html', context)


def event(request, event_id):
    event = get_object_or_404(Event, pk=event_id)
    event_context = {
        'event': event,
    }
    return render(request, 'events/event.html', event_context)

