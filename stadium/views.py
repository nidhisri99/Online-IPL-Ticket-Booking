import io

from django.http import FileResponse
from django.shortcuts import render

# Create your views here.
def stadium(request):
    return render(request,'printticket.html')


