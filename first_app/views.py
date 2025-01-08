from datetime import datetime
from django.shortcuts import redirect, render
from .models import Contact

# Create your views here.

def home(req):
    return render(req, 'pages/index.html')

def about(req):
    return render(req, 'pages/about.html')

def blog(req):
    return render(req, 'pages/blog.html')

def shop(req):
    return render(req, 'pages/shop.html')

def contact(req):
    if req.method == 'POST':
        nom = req.POST.get('nom')
        email = req.POST.get('email')
        sujet = req.POST.get('sujet')
        message = req.POST.get('message')
        
        newContact = Contact(
            nom=nom, 
            email=email, 
            sujet=sujet, 
            date =  datetime.now(),
            message=message
        )
        newContact.save()
        
        
        return redirect('Contact')    
    return render(req, 'pages/contact.html')

