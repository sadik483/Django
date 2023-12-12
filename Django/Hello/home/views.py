from django.shortcuts import render,HttpResponse
from datetime import datetime
from home.models import Contact
from django.contrib import messages

MESSAGE_TAGS = {
    messages.INFO: "",
    50: "critical",
} # Create your views here.

def index(request):
    context={
        'x':'This is varaible'
        }
    return render(request,'index.html')
    # return HttpResponse("This is home page")
def about(request):
    # return HttpResponse("This is about page")
    return render(request,'about.html')
def contact(request):
    # return HttpResponse("This is contact page")
    if request.method=='POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        subject=request.POST.get('subject')
        message=request.POST.get('message')
        contact=Contact(name=name,email=email,subject=subject,message=message,date=datetime.today())
        contact.save()
        messages.success(request,"Your message has been sent...")
    return render(request,'contact.html')