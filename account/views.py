from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth 
#from .models import UserProfile

# Create your views here.
#            
def home(request):
    pass    

def logout(request):
    auth.logout(request)
    return redirect('/tickets')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username =username , password = password)
        if user is not None:
            auth.login(request,user)
            return redirect('/tickets')
        else:
            messages.info(request,'invalid crediatials') 
            return redirect('login')       
    else:

        return render(request, 'login.html')


def register(request):

    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        confirm_password = request.POST['confirm_password']
        #phnumber = request.POST['phnumber']
        
        if password1 == confirm_password:
            if User.objects.filter(username=username).exists():
                messages.info(request,'username already exist')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'email already exist')
                return redirect('register')
            # elif User.objects.filter(phnumber=phnumber).exists():
            #           messages.info(request, 'An account exists with that phone number')
            #           return redirect('/accounts/register/')
            else:
                user = User.objects.create_user(username=username, password=password1, email=email)
                # user_profile = UserProfile.objects.create(phnumber=phnumber)
                # user_profile.phoneNumber = phnumber
                # user_profile.save()
                # user.save()
                messages.info(request, 'user created')
                return redirect('login')
                

        else:
            messages.info(request, 'password not matching')
            return redirect('register')
        return redirect('/')
    else:

        return render(request, 'register.html')
