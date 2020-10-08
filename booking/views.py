from django.shortcuts import render,redirect
from booking.models import booking_tickets
from django.contrib import messages
from django.contrib.auth.models import User,auth
from tickets.models import ticket_home

# Create your views here.

def booking(request):
            book = booking_tickets.objects.all()
            tics = ticket_home.objects.all()
            
            if request.method == 'POST':
                Match_name = request.POST['Match_name']
                # B_id = request.POST['B_id']
                No_of_tickets = request.POST['No_of_tickets']
                Seats =request.POST['Selected_seats']
                Price = request.POST['Price']
                date = request.POST['date']
        
                queryset1 = booking_tickets(match_name=Match_name, no_of_tickets=No_of_tickets,select_seats=Seats, total_price=Price, match_date=date)
                queryset1.save()
                return redirect('/payment')
                
            else:     
                 return render(request,"booking1.html",{"booking": tics})
