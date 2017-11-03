from django.contrib import admin
from lodge.models.models import *



class PaymentAdmin(admin.ModelAdmin):
	fields = ('payment_data')

class DueAdmin(admin.ModelAdmin):
	fields = ('date', 'date_paid')

class MemberAdmin(admin.ModelAdmin):
	fields = ('first_name', 'last_name', 'date_joined', 'active', 'payment', 'due')

class EventsAdmin(admin.ModelAdmin):
	fields = ('title', 'date', 'attendence', 'location' )



