from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.template import RequestContext
from django.http import HttpResponse
from django.conf import settings
from django.core.mail import send_mail, BadHeaderError
from django.core.mail import mail_admins
from wsgiref.util import FileWrapper
import operator
from django import forms
from lodge.forms.forms import *
from lodge.models.models import *
from lodge.decorators.decorators import check_recaptcha

@check_recaptcha
def add_inquiry(request):

    if request.method == 'GET':
        template_name = 'user/inquiry.html'
        inquiry_form = InquiryForm()
        return render(request, template_name, {'inquiry_form': inquiry_form})

    elif request.method == 'POST':
        form_data = request.POST
        inquiry_form = InquiryForm(form_data)

        
        if inquiry_form.is_valid() and request.recaptcha_is_valid:
            i = Inquiry(
                inquirer_first_name = inquiry_form.cleaned_data['inquirer_first_name'],
                inquirer_last_name = inquiry_form.cleaned_data['inquirer_last_name'],
                inquiry_title  = inquiry_form.cleaned_data['inquiry_title'],
                inquiry_content = inquiry_form.cleaned_data['inquiry_content'],
                inquiry_email_address = inquiry_form.cleaned_data['inquiry_email_address'],
            ) 

            i.save()
            
            subject = "Elk Lodge Inquiry"
            message = "This is a confirmation of your recent inquiry to the Elk Lodge"
            from_email = "imfakeinquiry@email.com"
            recipient = inquiry_form.cleaned_data['inquiry_email_address']
            recipient_list = [recipient]

            try:
                send_mail(subject, message, from_email, recipient_list)
                mail_admins(subject, message, fail_silently=False, connection=None, html_message=None)
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return HttpResponseRedirect('/success')
        else:
            return HttpResponse('Make sure all fields are entered and valid.')
            return HttpResponseRedirect('/error')

@check_recaptcha
def wedding(request):

    if request.method == 'GET':
        template_name = 'wedding/weddings.html'
        inquiry_form = InquiryForm()
        return render(request, template_name, {'inquiry_form': inquiry_form})

    elif request.method == 'POST':
        form_data = request.POST
        inquiry_form = InquiryForm(form_data)

        
        if inquiry_form.is_valid() and request.recaptcha_is_valid:
            i = Inquiry(
                inquirer_first_name = inquiry_form.cleaned_data['inquirer_first_name'],
                inquirer_last_name = inquiry_form.cleaned_data['inquirer_last_name'],
                inquiry_title  = inquiry_form.cleaned_data['inquiry_title'],
                inquiry_content = inquiry_form.cleaned_data['inquiry_content'],
                inquiry_email_address = inquiry_form.cleaned_data['inquiry_email_address'],
            ) 

            i.save()
            
            subject = "Elk Lodge Inquiry"
            message = "This is a confirmation of your recent inquiry to the Elk Lodge"
            from_email = "imfakeinquiry@email.com"
            recipient = inquiry_form.cleaned_data['inquiry_email_address']
            recipient_list = [recipient]

            try:
                send_mail(subject, message, from_email, recipient_list)
                mail_admins(subject, message, fail_silently=False, connection=None, html_message=None)
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return HttpResponseRedirect('/success')
        else:
            return HttpResponse('Make sure all fields are entered and valid.')
            return HttpResponseRedirect('/error')


@check_recaptcha
def add_subscriber_to_newsletter_list(request):
    if request.method == 'GET':
        template_name = 'user/newsletter.html'
        newsletter_form = NewsletterForm()
        return render(request, template_name, {'newsletter_form': newsletter_form})

    
    elif request.method == 'POST':

        form_data = request.POST
        newsletter_form = NewsletterForm(form_data)

        if newsletter_form.is_valid() and request.recaptcha_is_valid:
            n = Newsletter(
                subscriber_first_name = newsletter_form.cleaned_data['subscriber_first_name'],
                subscriber_last_name = newsletter_form.cleaned_data['subscriber_last_name'],
                subscriber_email_address = newsletter_form.cleaned_data['subscriber_email_address'],
            ) 

            n.save()
            
            subject = "Elk Lodge Newsletter Subscription request"
            message = "This is a confirmation of your Newsletter subscription request"
            from_email = "imfakenewslettertest@email.com"
            recipient = newsletter_form.cleaned_data['subscriber_email_address']
            recipient_list = [recipient]
            try:
                send_mail(subject, message, from_email, recipient_list)
                mail_admins(subject, message, fail_silently=False, connection=None, html_message=None)
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return HttpResponseRedirect('/success')
        else:
            return HttpResponse('Make sure all fields are entered and valid.')
            return HttpResponseRedirect('/error')
