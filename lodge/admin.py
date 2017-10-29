from django.contrib import admin

from . import models

admin.site.register(models.Elks)
admin.site.register(models.Photos)
admin.site.register(models.Payments)
admin.site.register(models.Donations)
admin.site.register(models.Events)
admin.site.register(models.Newsletter)

# Register your models here.
