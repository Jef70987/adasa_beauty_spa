from django.db import models
from django.contrib.auth.models import User

class service(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='services/')
    
    def __str__(self):
        return self.name
class ClientComment (models.Model):
    service = models.ForeignKey(service, on_delete=models.CASCADE)
    client_name = models.CharField(max_length=100)
    comment = models.TextField()
    rating = models.IntegerField()
    approved =models.BooleanField(default=False)
    
    def __str__(self):
        return f"{self.client_name} - {self.service.name}"
    
class Booking(models.Model):
    service = models.ForeignKey(service, on_delete=models.CASCADE)
    client_name = models.CharField(max_length=100)
    client_email = models.EmailField()
    Booking_date = models.DateTimeField()
    notes = models.TextField(blank=True)
    
    def __str__(self):
        return f"{self.client_name} - {self.service.name}"
    
class ContactInfo(models.Model):
    address = models.CharField(max_length=200)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    
    def __str__(self):
        return self.address
class About(models.Model):
    content = models.TextField()
    
    def __str__(self):
        return "About us"
    
    