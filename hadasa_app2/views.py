from django.shortcuts import*
from django.http import*
from .models import*
from django.core.mail import send_mail
from django.conf import settings
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializer import CommentSerializer

def main_fun(request,):
    services = service.objects.all()
    images = gallery.objects.all()
    time_status = available_time.objects.all()
    items = notification.objects.all()
    contact = ContactInfo.objects.all()
    context = {
        'services': services,
        'images': images,
        'time_status' : time_status,
        'items' : items,
        'contact' : contact,
    }
    #for booking form
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        contact = request.POST.get('contact')
        date = request.POST.get('date')
        population = request.POST.get('population')
        message = request.POST.get('message')

        email_message = f"""
        New booking Received From ADASA BEAUTY SPA
        ----------------------------------------------
        Client Details:
        -----------------------------------------------
        Name: {name}
        Email: {email}
        Contact: {contact}
        Booking Date: {date}
        Group size : {population}
        ------------------------------------------------
        Message :
        ---------
        {message}
        """
        send_mail(
            'ADASA BEAUTY SPA',#title
            email_message,#message
            'settings.Email_HOST_USER', #sender if not available
            [email],#receiver
            fail_silently=False
        )
        # Save to database
        Booking.objects.create(
            client_name=name,
            client_email=email,
            phone=contact,
            Booking_date=date,
            clients=population,
            notes=message or ""
        )
        return render(request,'booking.html')
    return render(request, 'index.html',context)

@api_view(['GET'])
def get_comments(request):
    items = ClientComment.objects.all()
    serializer = CommentSerializer(items, many=True)
    return Response(serializer.data)



