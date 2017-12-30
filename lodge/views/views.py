from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.template import RequestContext
from django.http import HttpResponse
from django.shortcuts import redirect
import operator
from datetime import date
from django import forms
from lodge.forms.forms import *
from django.db.models import Q
from lodge.models.models import *
from django.conf import settings
import braintree
from django.core.mail import send_mail, BadHeaderError
from django.core.mail import mail_admins
from wsgiref.util import FileWrapper




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
	today = date.today()
	today_filter =  Events.objects.filter(event_date__year=today.year)
	return render(request, template_name, {'members': all_members, 'events': all_events, 'today': today_filter})

def login(request):
	template_name = 'user/login.html'
	return render(request, template_name, {})

def wedding(request):
	template_name = 'wedding/weddings.html'
	return render(request, template_name, {})

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
	data = form.dict()
	result = braintree.Transaction.sale({
	'amount': data['amount'],
	'payment_method_nonce': data['payment_method_nonce'],
	'options': {
	"submit_for_settlement": True
	}
	})
	if result.is_success or result.transaction:
		return redirect('show_checkout', transaction_id=result.transaction.id)
	else:
		for x in result.errors.deep_errors: flash('Error: %s: %s' % (x.code, x.message))
		return redirect('new_checkout')


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
        template_name = '404.html'
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

def add_inquiry(request):
    if request.method == 'GET':
        template_name = 'user/inquiry.html'
        inquiry_form = InquiryForm()
        return render(request, template_name, {'inquiry_form': inquiry_form})

    elif request.method == 'POST':
        form_data = request.POST
        inquiry_form = InquiryForm()

        
        i = Inquiry(
            inquirer_first_name = form_data['inquirer_first_name'],
            inquirer_last_name = form_data['inquirer_last_name'],
            inquiry_title  = form_data['inquiry_title'],
            inquiry_content = form_data['inquiry_content'],
            inquiry_email_address = form_data['inquiry_email_address'],
        ) 

        i.save()
        
        botcheck = 'yes'
        subject = "Elk Lodge Inquiry"
        message = "This is a confirmation of your recent inquiry to the Elk Lodge"
        from_email = "imfake@email.com"
        recipient = form_data['inquiry_email_address']
        recipient_list = [recipient]
        if subject and message and recipient_list and botcheck == 'yes':
            try:
                send_mail(subject, message, from_email, recipient_list)
                mail_admins(subject, message, fail_silently=False, connection=None, html_message=None)
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return HttpResponseRedirect('/success')
        else:
            return HttpResponse('Make sure all fields are entered and valid.')
            return HttpResponseRedirect('/error')



    
