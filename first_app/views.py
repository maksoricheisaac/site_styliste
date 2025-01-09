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

def product_details(req, product_id):
    return render(req, 'pages/product_detail.html')

def contact(req):
    if req.method == 'POST':
        name = req.POST.get('name')
        email = req.POST.get('email')
        subject = req.POST.get('subject')
        message = req.POST.get('message')
        
        newContact = Contact(
            name=name, 
            email=email, 
            subject = subject ,
            date =  datetime.now(),
            message=message
        )
        newContact.save()
        
        
        return redirect('Contact')    
    return render(req, 'pages/contact.html')


