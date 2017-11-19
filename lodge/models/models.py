from django.db import models
from django.contrib.auth.models import *

# Create your models here.
class Photos(models.Model):
	photo_name = models.CharField(max_length=50)
	photo_url = models.CharField(max_length=100)
	photo_type = models.CharField(max_length=150)

	def __str__(self):
		return self.photo_name

	def __str__(self):
		return self.photo_url

class Elks(models.Model):
	first_name = models.CharField(max_length=50)
	last_name = models.CharField(max_length=50)
	nickname = models.CharField(max_length=20)
	email_address = models.CharField(max_length=50)
	linked_in_url = models.CharField(max_length=50)
	date_joined = models.DateField()
	elk_photo = models.ForeignKey(Photos, on_delete=models.CASCADE)

	def __str__(self):
		return self.first_name

	def __str__(self):
		return self.last_name

	def __str__(self):
		return self.nickname

	def __str__(self):
		return self.email_address

	def __str__(self):
		return self.linked_in_url

	def __str__(self):
		return self.date_joined

	def __str__(self):
		return self.elk_photo


class Donations(models.Model):
	donation_type = models.CharField(max_length=50)
	donation_amount = models.CharField(max_length=50)
	donation_date = models.DateField()

	def __str__(self):
		return self.donation_type

	def __str__(self):
		return self.donation_amount

	def __str__(self):
		return self.donation_date

class Payments(models.Model):
	payment_name = models.CharField(max_length=50)
	payment_method = models.CharField(max_length=150)
	payment_total_amount = models.CharField(max_length=10)
	payment_date = models.DateField()
	payment_time = models.CharField(max_length=20)

	def __str__(self):
		return self.payment_name

	def __str__(self):
		return self.payment_method

	def __str__(self):
		return self.payment_total_amount

	def __str__(self):
		return self.payment_date

	def __str__(self):
		return self.payment_time

class Events(models.Model):
	event_name = models.CharField(max_length=50)
	event_type = models.CharField(max_length=50)
	event_description = models.TextField()
	event_date = models.DateField()
	event_location = models.CharField(max_length=100)
	event_time = models.CharField(max_length=20)

	def __str__(self):
		return self.event_name

	def __str__(self):
		return self.event_type

	def __str__(self):
		return self.event_description

	def __str__(self):
		return self.event_date

	def __str__(self):
		return self.event_location

	def __str__(self):
		return self.event_time

class Newsletter(models.Model):
	subscriber_first_name = models.CharField(max_length=50)
	subscriber_last_name = models.CharField(max_length=50)
	subscriber_email_address = models.CharField(max_length=50)

	def __str__(self):
		return self.subscriber_first_name

	def __str__(self):
		return self.subscriber_last_name

	def __str__(self):
		return self.subscriber_email_address

class Inquiry(models.Model):
	inquirer_first_name = models.CharField(max_length=50)
	inquirer_last_name = models.CharField(max_length=50)

	def __str__(self):
		return self.inquirer_first_name

	def __str__(self):
		return self.inquirer_last_name






