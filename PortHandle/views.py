
from django.shortcuts import render, redirect
from PortHandle.models import Contact
from django.contrib import messages
# Create your views here.
def home(request):
    return render(request,'index.html')
def contact(request):
    if request.method =="POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        msg = request.POST.get('msg')
        con = Contact(name=name,mail=email,subject=subject,msg=msg)
        con.save()
        messages.success(request,'Message Sent Successfully !')
    return redirect('Home')
    