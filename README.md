# Online-IPL-Ticket-Booking
DBMS-Mini Project 

# Introduction

The goal of this project is to provide minimalistic django project template that everyone can use, which _just works_ out of the box and has the basic setup you can expand on. 

Template is written with Django 3.0.4 and python 3 in mind.

![Default Home View](__screenshots/home.png?raw=true "Title")

### Main features

* Separated dev and production settings

* Example app with custom user model

* Bootstrap static files included

* User registration and logging in as demo

* Procfile for easy deployments

* Separated requirements files

* SQLite by default if no env variable is set

# Usage

To use this template to start your own project:

### Existing virtualenv

If your project is already in an existing python3 virtualenv first install django by running

    $ pip install django
    
And then run the `django-admin.py` command to start the new project:

    $ django-admin.py startproject \
      --template=https://github.com/nidhisri99/Online-IPL-Ticket-Booking/ \
      --extension=py,md \
      <project_name>
      
### No virtualenv

This assumes that `python3` is linked to valid installation of python 3 and that `pip` is installed and `pip3`is valid
for installing python 3 packages.

Installing inside virtualenv is recommended, however you can start your project without virtualenv too.

If you don't have django installed for python 3 then run:

    $ pip3 install django
    
And then:

    $ python3 -m django startproject \
      --template=https://github.com/nidhisri99/Online-IPL-Ticket-Booking \
      --extension=py,md \
      <project_name>
      
      
After that just install the local dependencies, run migrations, and start the server.



# Getting Started

First clone the repository from Github and switch to the new directory:

    $ git clone https://github.com/nidhisri99/Online-IPL-Ticket-Booking/.git
    $ cd Online-IPL-Ticket-Booking
    
Activate the virtualenv for your project.
    
Install project dependencies:

    $ pip install -r requirements/local.txt
    
    
Then simply apply the migrations:

    $ python manage.py migrate
    

You can now run the development server:

    $ python manage.py runserver
![Alt text](/Online-IPL-ticket%20Booking%20Images/register.png?raw=true "Optional Title")
![Alt text](/Online-IPL-ticket%20Booking%20Images/login.png?raw=true "Optional Title")
![Alt text](/Online-IPL-ticket%20Booking%20Images/home%20page.png?raw=true "Optional Title")
![Alt text](/Online-IPL-ticket%20Booking%20Images/ticket%20available.png?raw=true "Optional Title")
![Alt text](/Online-IPL-ticket%20Booking%20Images/booking.png?raw=true "Optional Title")
![Alt text](/Online-IPL-ticket%20Booking%20Images/select%20seat.png?raw=true "Optional Title")
![Alt text](/Online-IPL-ticket%20Booking%20Images/payment.png?raw=true "Optional Title")
![Alt text](/Online-IPL-ticket%20Booking%20Images/print%20ticket.png?raw=true "Optional Title")
