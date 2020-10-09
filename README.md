# Online-IPL-Ticket-Booking
DBMS-Mini Project 

# Introduction

The “IPL Ticket Booking System” has been developed to override the problems prevailing in the practicing manual system. This software is supported to eliminate and in some case reduce the hardships faced by the existing system. Moreover this system is designed for the particular need of the company to carry out operations in a smooth and effective manner.
The application is reduced as much as possible to avoid errors while entering the data. It also provides error message while entering invalid data. No formal knowledge is needed for the user to use this system. Thus by this all it proves that it is user-friendly. IPL Ticket Booking System, as described above, can lead to error free, secure, reliable and fast management system. It can assist the user to concentrate on their other activities rather to concentrate on the record keeping. Thus it will help organization in better utilization of resource.


###Technologies Used: 
	HTML: Page layout has been designed in HTML.
	CSS: CSS has been used for all the designing part.
	JavaScript: All the validation task and animations has been developed by JavaScript.
	Python : All the business logic has been implemented in python
	MySQL: MySQL database has been used as database for the project.
	Django: Project has been developed over the Django Framework.


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
![Alt text](/Online-IPL-ticket%20Booking%20Images/tickets%20avaliable.png?raw=true "Optional Title")
![Alt text](/Online-IPL-ticket%20Booking%20Images/booking.png?raw=true "Optional Title")
![Alt text](/Online-IPL-ticket%20Booking%20Images/gate.png?raw=true "Optional Title")
![Alt text](/Online-IPL-ticket%20Booking%20Images/select%20seat.png?raw=true "Optional Title")
![Alt text](/Online-IPL-ticket%20Booking%20Images/payment.png?raw=true "Optional Title")
![Alt text](/Online-IPL-ticket%20Booking%20Images/print%20ticket.png?raw=true "Optional Title")
