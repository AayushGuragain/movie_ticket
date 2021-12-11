'''
Here we register the models created, so we can add our data from /admin by logging in.
'''

from django.contrib import admin
from .models import Ticket, Booking
# Register your models here.

admin.site.register(Ticket)
admin.site.register(Booking)
