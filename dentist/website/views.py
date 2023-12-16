from django.shortcuts import render
from django.core.mail import send_mail

# Create your views here.

def home(request):
    return render(request, 'home.html', {})

def contact(request):     
    print(request.POST['message-name'])
    if request.POST == "POST":
        message_email = request.POST['message-email']
        message_name = request.POST['message-name']
        message = request.POST['message']

        send_mail('Creación de cita',
                  message,
                  message_email,
                  ['krisalidaf@gmail.com', 'rtobiasgm@gmail.com'],)
        
        return render(request, 'contact.html', {'message_name': message_name})
    else: 
        return render(request, 'contact.html', {})

