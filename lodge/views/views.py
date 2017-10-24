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
    return HttpResponse("Hello, world. You're at the index.")

def about(request):
	template_name = 'about.html' 
	return render(request, template_name, {})

def events(request):
	template_name = 'events.html' 
	return render(request, template_name, {})

def membership(request):
	template_name = 'membership.html' 
	return render(request, template_name, {})
