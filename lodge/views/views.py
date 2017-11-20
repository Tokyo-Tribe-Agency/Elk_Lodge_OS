from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.template import RequestContext
from django.http import HttpResponse
import operator
from datetime import date
from django import forms
from django.db.models import Q
from lodge.models.models import *

# Create your views here.

def index(request):
	template_name = 'index.html'
	all_members = Elks.objects.all() 
	all_events = Events.objects.all()
	print("request", request.path)	
	today = date.today()
	today_filter =  Events.objects.filter(event_date__year=today.year)
	for events in today_filter:
		print("name", events.event_name)
	return render(request, template_name, {'members': all_members, 'events': all_events, 'today': today_filter})

def login(request):
	template_name = 'login.html'
	return render(request, template_name, {})

def wedding(request):
	template_name = 'weddings.html'
	return render(request, template_name, {})

def register(request):
	template_name = 'register.html'
	print("request", request.path)
	return render(request, template_name, {})

# def about(request):
# 	template_name = 'about.html'
# 	return render(request, template_name, {'members' : all_members})

# def events(request):
# 	template_name = 'events.html' 
# 	return render(request, template_name, {'events' : all_events})

# def recent_events(request):
# 	template_name = 'slide.html'
# 	return render(request, template_name, {'events': today_filter})

