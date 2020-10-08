from django.shortcuts import render
from django.contrib import messages

# Create your views here.
def cancel(request):
    # messages.info(request,'3working days') 
    return render(request,"cancel_tickets.html")