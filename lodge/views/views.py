from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.template import RequestContext
from django.http import HttpResponse
import operator
from django import forms
from django.db.models import Q
from lodge.models.models import *

# Create your views here.

def index(request):
	template_name = 'index.html' 
	return render(request, template_name, {})

def about(request):
	template_name = 'about.html'
	all_members = Member.objects.all() 
	return render(request, template_name, {'members' : all_members})

def events(request):
	template_name = 'events.html' 
	all_events = Event.objects.all()
	no_ono = Event.objects.filter(attendence__pk = 1).distinct()
	print("sup", no_ono)
	return render(request, template_name, {'events' : all_events, 'no_ono': no_ono})

def membership(request):
	template_name = 'membership.html' 
	all_members = Member.objects.all()
	return render(request, template_name, {'member': all_members})
