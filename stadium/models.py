from django.db import models

# Create your models here.
class stadium(models.Model):
    s_id =models.IntegerField()
    t_id = models.IntegerField()
    s_name = models.CharField(max_length = 100)
    location = models.CharField(max_length = 100)
    no_of_seats = models.IntegerField()