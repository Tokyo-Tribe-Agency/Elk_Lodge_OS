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
	return render(request, template_name, {})

def about(request):
	template_name = 'about.html'
	all_members = Elks.objects.all() 
	return render(request, template_name, {'members' : all_members})

def events(request):
	template_name = 'events.html' 
	all_events = Events.objects.all()
	return render(request, template_name, {'events' : all_events})

def recent_events(request):
	today = date.today()
	today_filter =  Events.objects.filter(event_date__year=today.year)
	template_name = 'slide.html'
	return render(request, template_name, {'events': today_filter})

def membership(request):
	template_name = 'membership.html' 
	all_members = Member.objects.all()
	return render(request, template_name, {'member': all_members})
