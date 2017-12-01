from django.db import models
from django.contrib.auth.models import *
from django.utils import timezone
import datetime
from decimal import Decimal


# Create your models here.
class Photos(models.Model):
	photo_name = models.CharField(max_length=50, null=True, blank=True)
	photo_url = models.CharField(max_length=100, null=True, blank=True)
	photo_type = models.CharField(max_length=150, null=True, blank=True)
	photo_description = models.CharField(max_length=300, null=True, blank=True)


	def __str__(self):
		return self.photo_name

	# def __str__(self):
	# 	return self.photo_url

	# def __str__(self):
	# 	return self.photo_type

	# def __str__(self):
	# 	return self.photo_description

class Elks(models.Model):
	member_type = models.CharField(max_length=50, null=True, blank=True)
	first_name = models.CharField(max_length=20, null=True, blank=True)
	last_name = models.CharField(max_length=50, null=True, blank=True)
	nickname = models.CharField(max_length=30, null=True, blank=True)
	email_address = models.CharField(max_length=100, null=True, blank=True)
	linked_in_url = models.CharField(max_length=100, null=True, blank=True)
	date_joined = models.DateField('date joined', null=True, blank=True)
	elk_photo = models.ForeignKey(Photos, on_delete=models.CASCADE)

	def __str__(self):
		return self.first_name

	# def __str__(self):
	# 	return self.last_name

	# def __str__(self):
	# 	return self.nickname

	# def __str__(self):
	# 	return self.email_address

	# def __str__(self):
	# 	return self.linked_in_url

	# def __str__(self):
	# 	return self.date_joined

	# def __str__(self):
	# 	return self.elk_photo

	def was_added_recently(self):
		return self.elk_member_since_date >= timezone.now() - datetime.timedelta(days=1)


class Donations(models.Model):
	donation_type = models.CharField(max_length=100, null=True, blank=True)
	donation_amount = models.DecimalField(max_digits=30, decimal_places=2, null=True, blank=True)
	donation_date = models.DateField(null=True, blank=True)

	def __str__(self):
		return self.donation_type

	# def __str__(self):
	# 	return self.donation_amount

	# def __str__(self):
	# 	return self.donation_date


class Payments(models.Model):
	payment_name = models.CharField(max_length=50, null=True, blank=True)
	payment_method = models.CharField(max_length=150, null=True, blank=True)
	payment_total_amount = models.CharField(max_length=10, null=True, blank=True)
	payment_date = models.DateField(null=True, blank=True)
	payment_time = models.CharField(max_length=20, null=True, blank=True)

	def __str__(self):
		return self.payment_name

	# def __str__(self):
	# 	return self.payment_method

	# def __str__(self):
	# 	return self.payment_total_amount

	# def __str__(self):
	# 	return self.payment_date

	# def __str__(self):
	# 	return self.payment_time

class Events(models.Model):
	event_name = models.CharField(max_length=50, null=True, blank=True)
	event_type = models.CharField(max_length=100, null=True, blank=True)
	event_description = models.TextField(null=True, blank=True)
	event_date = models.DateTimeField('date of event')
	event_location = models.CharField(max_length=100, null=True, blank=True)
	event_time = models.CharField(max_length=20, null=True, blank=True)
	event_amount = models.DecimalField(max_digits=30, decimal_places=2, null=True, blank=True)

	def __str__(self):
		return self.event_name

	# def __str__(self):
	# 	return self.event_type

	# def __str__(self):
	# 	return self.event_description

	# def __str__(self):
	# 	return self.event_date

	# def __str__(self):
	# 	return self.event_location

	# def __str__(self):
	# 	return self.event_time

	# def __str__(self):
	# 	return self.event_amount


class Newsletter(models.Model):
	subscriber_first_name = models.CharField(max_length=20, null=True, blank=True)
	subscriber_last_name = models.CharField(max_length=50, null=True, blank=True)
	subscriber_email_address = models.CharField(max_length=100, null=True, blank=True)
	new_subscriber = models.CharField(max_length=1, null=True, blank=True)
	newsletter_title = models.CharField(max_length=200, null=True, blank=True)
	archive_urls = models.CharField(max_length=100, null=True, blank=True)
	archive_date = models.DateTimeField('elk newsletter date', null=True, blank=True)

	# def __str__(self):
	# 	return self.subscriber_first_name

	# def __str__(self):
	# 	return self.subscriber_last_name

	def __str__(self):
		return self.subscriber_email_address

	# def __str__(self):
	# 	return self.new_subscriber

	# def __str__(self):
	# 	return self.newsletter_title

	# def __str__(self):
	# 	return self.archive_urls

	# def __str__(self):
	# 	return str(self.archive_date)

class Inquiry(models.Model):
	inquirer_first_name = models.CharField(max_length=20, null=True, blank=True)
	inquirer_last_name = models.CharField(max_length=50, null=True, blank=True)
	inquiry_title = models.CharField(max_length=250, null=True, blank=True)
	inquiry_content = models.CharField(max_length=500, null=True, blank=True)
	inquiry_email_address = models.CharField(max_length=100, null=True, blank=True)

	# def __str__(self):
	# 	return self.inquirer_first_name

	# def __str__(self):
	# 	return self.inquirer_last_name

	def __str__(self):
		return self.inquiry_email_address

	# def __str__(self):
	# 	return self.inquiry_title

	# def __str__(self):
	# 	return self.inquiry_content


class Membership_Application(models.Model):
	prospective_member_first_name = models.CharField(max_length=20, null=True, blank=True)
	prospective_member_last_name = models.CharField(max_length=50, null=True, blank=True)
	prospective_member_email_address = models.CharField(max_length=100, null=True, blank=True)
	prospective_member_address = models.CharField(max_length=300, null=True, blank=True)
	prospective_membership_type = models.CharField(max_length=100, null=True, blank=True)

	# def __str__(self):
	# 	return self.prospective_member_first_name

	# def __str__(self):
	# 	return self.prospective_member_last_name

	def __str__(self):
		return self.prospective_member_email_address

	# def __str__(self):
	# 	return self.prospective_member_address

	# def __str__(self):
	# 	return self.prospective_membership_type

class PayPal_Transaction(models.Model):
    trans_id = models.CharField(max_length=20, null=True, blank=True)
    trans_type = models.CharField(max_length=20, null=True, blank=True)
    amount = models.DecimalField(max_digits=30, decimal_places=2, null=True, blank=True)
    status = models.CharField(max_length=20, null=True, blank=True)
    created_at = models.DateTimeField('Transaction Created', null=True, blank=True)
    updated_at = models.DateTimeField('Transaction Last Updated', null=True, blank=True)

    def __str__(self):
        return str(self.trans_id)

class PayPal_Payment(models.Model):
    token = models.CharField(max_length=20, null=True, blank=True)
    bin = models.CharField(max_length=20, null=True, blank=True)
    last_4 = models.IntegerField(default=0, null=True, blank=True)
    card_type = models.CharField(max_length=20, null=True, blank=True)
    expiration_date = models.IntegerField(default=0, null=True, blank=True)
    cardholder_name = models.CharField(max_length=50, null=True, blank=True)
    customer_location = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return str(self.token)



