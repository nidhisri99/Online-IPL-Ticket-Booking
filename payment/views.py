from django.shortcuts import render,redirect
from .models import payment
# from booking.models import booking_tickets


# Create your views here.

def payment_(request):
            
            if request.method == "POST":
                CardNumber = request.POST['CardNumber']
                NameInCard = request.POST['NameInCard']
                CVV = request.POST['CVV']
                MM = request.POST['MM']
                YY =request.POST['YY']
                Price = request.POST['Price']
                
                queryset2 = payment(CardNumber=CardNumber, NameInCard=NameInCard, CVV=CVV,MM=MM,YY=YY,Price= Price)
                queryset2.save()
                return redirect('/printtickets')
            else:
                return render(request,"payment.html")