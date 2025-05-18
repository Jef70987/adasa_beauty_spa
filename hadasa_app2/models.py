from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class service(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='services/')
    
    def __str__(self):
        return (self.description)

class ClientComment (models.Model):
    client_name = models.CharField(max_length=100)
    service = models.ForeignKey(service, on_delete=models.CASCADE)
    rating = models.IntegerField()
    comment = models.TextField()
    date = models.DateTimeField(default=timezone.now)
    reply = models.TextField(default='Thanks for the reply')
    def __str__(self):
        return f"{self.client_name} - {self.service.name}"
    
class Booking(models.Model):
    client_name = models.CharField(max_length=100)
    client_email = models.EmailField()
    Booking_date = models.DateTimeField()
    notes = models.TextField(blank=True)
    phone = models.CharField(null=False)
    clients = models.IntegerField(default=1)
    def __str__(self):
        return f"{self.client_name} - {self.clients}"
    
class ContactInfo(models.Model):
    address = models.CharField(max_length=200)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    def __str__(self):
        return self.address



class gallery(models.Model):
    image = models.ImageField(upload_to='gallery/')
    upload_date = models.DateTimeField()
    def __str__(self):
        return f"{self.image} - {self.upload_date}"

class available_time(models.Model):
    status = [('open','open'),('closed','closed')]
    days = models.CharField(max_length=20)
    time_open = models.TimeField()
    time_closed = models.TimeField()
    current_status = models.CharField(max_length=20, choices=status, default='open')

class notification(models.Model):
    notification = models.TextField()