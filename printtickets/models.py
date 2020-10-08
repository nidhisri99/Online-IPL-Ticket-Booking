from django.db import models

# Create your models here.
class print_tickets(models.Model):
    objects = models.Manager()
    
    matchfullname = models.CharField(max_length = 50)
    gate = models.IntegerField()
    seat_numbers = models.CharField(max_length=20)
    match_number = models.IntegerField()
    match_time= models.TimeField()
    location = models.CharField(max_length = 50)
    match_image = models.ImageField()
