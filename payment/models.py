from django.db import models

# Create your models here.
class payment(models.Model):
    objects = models.Manager()

    
    CardNumber = models.IntegerField()
    NameInCard = models.CharField(max_length = 30)
    CVV = models.IntegerField()
    MM = models.IntegerField()
    YY = models.IntegerField()
    Price = models.IntegerField()
  