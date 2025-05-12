from django.contrib import admin
from .models import service, ClientComment, Booking, ContactInfo,About

@admin.register(service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('name','price')
    
@admin.register(ClientComment)
class ClientComment(admin.ModelAdmin):
    list_display = ('client_name', 'service','rating', 'approved')
    list_editable = ('approved',)
    
@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('client_name','service','Booking_date')
    
@admin.register(ContactInfo)
class ContactInfoAdmin(admin.ModelAdmin):
    list_display = ('address','phone','email')
    
@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ('content',)
