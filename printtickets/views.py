import io

from django.http import FileResponse
from .models import print_tickets
#from reportlab.pdfgen import canvas
from django.shortcuts import render,redirect

# Create your views here.
def printticket(request):
    if request.method == "POST":
        matchfullname = request.POST['matchfullname']
        gate = request.POST['gate']
        seat_numbers= request.POST['seat_numbers']
        match_number= request.POST['match_number']
        match_time= request.POST['match_time']
        location= request.POST['location']
        match_image= request.POST['match_image']

        queryset3 = print_tickets(matchfullname=matchfullname,gate = gate,seat_numbers =seat_numbers,match_number=match_number,match_time=match_time,location=location,match_image=match_image)
        queryset3.save()

        return redirect('/tickets')
        
    else:
        return render(request,'printticket.html') 
           
       
