from django.shortcuts import render
from .models import ticket_home

# Create your views here.



def index(request):
    
    tics = ticket_home.objects.all()

    return render(request,"index.html",{'tics':tics})

  