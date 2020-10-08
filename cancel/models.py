from django.db import models

# Create your models here.
class cancel(models.Model):
    
    match_name = models.CharField(max_length=20)