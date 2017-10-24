from django.db import models
from django.contrib.auth.models import *

# Create your models here.
class Payment(models.Model):
	payment_data = models.CharField(max_length=100)

class Due(models.Model):
	date = models.DateField()
	date_paid = models.DateField()

class Member(models.Model):
	first_name = models.CharField(max_length = 50)
	last_name = models.CharField(max_length = 50)
	date_joined = models.DateField()
	active = models.BooleanField()
	payment = models.ForeignKey(Payment)
	due = models.ForeignKey(Due)


class Events(models.Model):
	title = models.CharField(max_length=100)
	date = models.DateField()
	attendence = models.ManyToManyField(Member)
	location = models.CharField(max_length=100)





