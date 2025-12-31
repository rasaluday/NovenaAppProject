from django.contrib import admin
from .models import *

# Register your models here.

@admin.register(contactModel)
class contactAdmin(admin.ModelAdmin):
    list_display=('name','email','subject','phoneNo','message')

@admin.register(Appointment)
class AppoinmentAdmin(admin.ModelAdmin):
    list_display=('full_name','department','doctor','appointment_date','appointment_time','phone_number','message','is_active','created_at')
    list_filter = ('department','doctor','appointment_date','is_active')
    search_fields=('full_name','phone_number','doctor')


@admin.register(SubscribeFotter)
class SubscribeFotter(admin.ModelAdmin):
    list_display=('email',)

@admin.register(SingleBlogModel)
class SingleBlogModelAdmin(admin.ModelAdmin):
    list_display=('name','email','message')
