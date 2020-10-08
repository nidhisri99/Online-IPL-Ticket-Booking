from django.urls import path

from . import views

urlpatterns = [
     path("register",views.register,name = "register"),
     path("login",views.login,name="login"),
     path("home" ,views.home, name="home"),
     #path("forgot_password",views.forgot_password,name="forgot_password"),
     path("logout",views.logout,name="logout"),
]