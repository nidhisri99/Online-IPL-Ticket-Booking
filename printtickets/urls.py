
from django.urls import path
from . import views

urlpatterns = [
    path('',views.printticket,name='printticket'),
    
    
]
