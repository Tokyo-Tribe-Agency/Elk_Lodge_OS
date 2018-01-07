from django.shortcuts import render
from django.shortcuts import redirect
import operator
from datetime import date
from lodge.models.models import *
from django.conf import settings

def index(request):
	template_name = 'index.html'
	all_members = Elks.objects.all() 
	all_events = Events.objects.all()
	today = date.today()
	today_filter =  Events.objects.filter(event_date__year=today.year)
	return render(request, template_name, {'members': all_members, 'events': all_events, 'today': today_filter})

def login(request):
	template_name = 'user/login.html'
	return render(request, template_name, {})

# def wedding(request):
# 	template_name = 'wedding/weddings.html'
# 	return render(request, template_name, {})

def newsletter(request):
    template_name = 'user/newsletter.html'
    return render(request, template_name, {})

def application(request):
    template_name = 'user/application.html'
    return render(request, template_name, {})

def register(request):
	template_name = 'user/register.html'
	print("request", request.path)
	return render(request, template_name, {})

def success(request):
    template_name = 'user/success.html'
    # print("request", request.path)
    return render(request, template_name, {})

def error(request):
    template_name = 'user/error.html'
    # print("request", request.path)
    return render(request, template_name, {})



    