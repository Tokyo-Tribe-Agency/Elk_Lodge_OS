from django.shortcuts import render
from django.shortcuts import redirect
from django import forms
from lodge.forms.forms import *
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

