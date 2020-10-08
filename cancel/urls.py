
from django.urls import path
from . import views

urlpatterns = [
    path('',views.cancel,name='cancel'),
    
]
