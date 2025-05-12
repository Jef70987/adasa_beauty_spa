from django.shortcuts import render, redirect
from .models import service, ClientComment, ContactInfo,About,Booking

def index(request):
    
    services = service.objects.all()
    comments = ClientComment.objects.filter(approved = True)
    contact_info = ContactInfo.objects.first()
    about = About.objects.first()
    return render(request,'index.html',{
        'services' :services,
        'comments':comments,
        'contact_info' : contact_info,
        'about' :about
    })
    
def book_service(request):
    if request.method == 'POST':
        service_id = request.POST['service']
        client_name = request.POST['name']
        client_email = request.POST['email']
        Booking_date = request.POST['date']
        notes = request.POST['notes']
        service = service.objects.get(id=service_id)
        Booking.objects.create (
            service=service,
            client_name=client_name,
            client_email=client_email,
            Booking_date = Booking_date,
            notes=notes
        )
        return redirect('index')
    return redirect('index')
