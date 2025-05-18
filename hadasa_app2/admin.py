from django.contrib import admin
from .models import *

@admin.register(service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('name','description','price','image')
    
@admin.register(ClientComment)
class ClientComment(admin.ModelAdmin):
    list_display = ('client_name', 'service','rating','comment')
    list_editable = ('comment',)
    
@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('client_name','client_email','Booking_date','notes','phone','clients')
@admin.register(ContactInfo)
class ContactInfoAdmin(admin.ModelAdmin):
    list_display = ('address','phone','email')
    

@admin.register(gallery)
class galleryAdmin(admin.ModelAdmin):
    list_display = ('image','upload_date')

admin.site.site_header = "ADASA SPA ADMIN"
admin.site.site_title = "Admin portal"

@admin.register(available_time)
class available_timeAdmin(admin.ModelAdmin):
    list_display = ('days','time_open','time_closed','current_status')
    list_editable =('time_open','time_closed','current_status')
@admin.register(notification)
class notificationAdmin(admin.ModelAdmin):
    list_display=('notification',)