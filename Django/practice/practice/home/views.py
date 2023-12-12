import datetime
from email import message
from django.shortcuts import render
from home.models import Contact
from datetime import datetime
# Create your views here.

def index(request):
    return render(request,'index.html')
def contact(request):
    if request.method=='POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        message=request.POST.get('message')
        contact=Contact(name=name,email=email,message=message,date=datetime.today())
        contact.save()
    return render(request,'contact.html')