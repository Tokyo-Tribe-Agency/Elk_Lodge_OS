from django.shortcuts import redirect, render
from lodge.models.models import *
from django.conf import settings
from django.db.models import Q
import operator



def archive(request):
    template_name = 'events/allevents.html' 
    events = Events.objects.order_by('event_date')
    return render(request, template_name, {'events': events})


def search_keywords(request):
    form_data = request.GET
    iterable_form_data = form_data.dict()
    search_box = iterable_form_data['Search']
    template_name = 'events/allevents.html'
    events_head = Events.objects.filter(event_description__contains=search_box)
    if events_head.exists():
        return render(request, template_name, {'events': events_head, 'search_box': search_box})
    else: 
        template_name = 'user/error.html'
        return render(request, template_name)

def filter_by_amount(request):
    events = Events.objects.order_by('event_amount')
    template_name = 'events/allevents.html'
    return render(request, template_name, {'events': events})    

def recent_events(request):
    events = Events.objects.order_by('event_date')[:5]
    template_name = 'events/allevents.html'
    return render(request, template_name, {'events': events})    

def get_this_event(request, event_id):
    template_name = 'events/event.html'
    event = Events.objects.get(pk= event_id)
    return render(request, template_name, {'event': event})
