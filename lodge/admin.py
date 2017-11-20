from django.contrib import admin
from lodge.models.models import *

admin.site.register(Photos)
admin.site.register(Elks)
admin.site.register(Donations)
admin.site.register(Payments)
admin.site.register(Events)
admin.site.register(Newsletter)
admin.site.register(Inquiry)
admin.site.register(PayPal_Transaction)
admin.site.register(PayPal_Payment)
admin.site.register(Membership_Application)

# class PaymentAdmin(admin.ModelAdmin):
# 	fields = ('payment_data')

# class DueAdmin(admin.ModelAdmin):
# 	fields = ('date', 'date_paid')

# class MemberAdmin(admin.ModelAdmin):
# 	fields = ('first_name', 'last_name', 'date_joined', 'active', 'payment', 'due')

# class EventsAdmin(admin.ModelAdmin):
# 	fields = ('title', 'date', 'attendence', 'location' )
