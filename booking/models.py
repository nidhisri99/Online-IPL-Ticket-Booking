from django.db import models

# Create your models here.
class booking_tickets(models.Model):
    objects = models.Manager()
    
    booking_id =models.IntegerField()
    match_name = models.CharField(max_length = 100)
    no_of_tickets = models.IntegerField()
    select_seats = models.CharField(max_length=10)
    total_price = models.IntegerField()
    match_date = models.DateField(null = True)