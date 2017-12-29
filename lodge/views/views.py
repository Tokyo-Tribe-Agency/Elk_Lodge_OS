from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.template import RequestContext
from django.http import HttpResponse
import operator
from datetime import date
from django import forms
from django.db.models import Q
from lodge.models.models import *
from django.conf import settings
import braintree



braintree.Configuration.configure(
    braintree.Environment.Sandbox,
    'dwnqbjvjdjc8ysjp',
    'kgzvv6qhfzq6dq5y',
    '4e0b90ddfad27f835c658a2f76850504'
)

TRANSACTION_SUCCESS_STATUSES = [
    braintree.Transaction.Status.Authorized,
    braintree.Transaction.Status.Authorizing,
    braintree.Transaction.Status.Settled,
    braintree.Transaction.Status.SettlementConfirmed,
    braintree.Transaction.Status.SettlementPending,
    braintree.Transaction.Status.Settling,
    braintree.Transaction.Status.SubmittedForSettlement
]
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

def new_checkout(request):
    client_token = braintree.ClientToken.generate()
    template_name = 'paypal/new.html'
    return render(request, template_name, {'client_token': client_token})

def show_checkout(request, transaction_id):
    transaction = braintree.Transaction.find(transaction_id)
    template_name = "paypal/show.html"
    result = {}
    if transaction.status in TRANSACTION_SUCCESS_STATUSES:
        result = {
            'header': 'Sweet Success!',
            'icon': 'success',
            'message': 'Your test transaction has been successfully processed. See the Braintree API response and try again.'
        }
    else:
        result = {
            'header': 'Transaction Failed',
            'icon': 'fail',
            'message': 'Your test transaction has a status of ' + transaction.status + '. See the Braintree API response and try again.'
        }

    return render(request, template_name, {'transaction': transaction, 'result': result})

def create_checkout(request):
	form = request.POST
	data = 
	
	result = braintree.Transaction.sale({
	'amount': request.form.cleaned_data['amount'],
	'payment_method_nonce': request.form.cleaned_data['payment_method_nonce'],
	'options': {
	"submit_for_settlement": True
	}
	})
	if result.is_success or result.transaction:
		return redirect('show_checkout', transaction_id=result.transaction.id)
	else:
		for x in result.errors.deep_errors: flash('Error: %s: %s' % (x.code, x.message))
		return redirect('new_checkout')



# def about(request):
# 	template_name = 'about.html'
# 	return render(request, template_name, {'members' : all_members})

# def events(request):
# 	template_name = 'events.html' 
# 	return render(request, template_name, {'events' : all_events})

# def recent_events(request):
# 	template_name = 'slide.html'
# 	return render(request, template_name, {'events': today_filter})

