from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.template import RequestContext
from django.http import HttpResponse
import operator
from django import forms
from django.db.models import Q
from lodge.models.models import *



# Create your views here.
