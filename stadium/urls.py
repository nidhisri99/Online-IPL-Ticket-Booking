
from django.urls import path
from . import views

urlpatterns = [
    path('',views.stadium,name='stadium'),
    #path('',views.download,name='download')
    
]
