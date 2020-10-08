from django.db import models

# Create your models here.
class ticket_home(models.Model):
    objects = models.Manager()

    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to='pics')
    date = models.DateField()
    location = models.CharField(max_length=100)
    fullName = models.CharField(max_length=100)
    m_no = models.IntegerField()
    start_time = models.TimeField()

# class ticket(models.Model):
#     t_id =models.IntegerField()
#     m_name = models.CharField(max_length = 100)
#     m_date = models.DateField()
#     m_no = models.IntegerField()
#     price = models.IntegerField()
#     seat_no = models.IntegerField()
#     location = models.CharField(max_length = 100)
#     gate_no = models.IntegerField()
#     start_time = models.TimeField()

# class booking(models.Model):
#     booking_id =models.IntegerField()
#     ticket_id = models.IntegerField()
#     match_name = models.CharField(max_length = 100)
#     no_of_tickets = models.IntegerField()
#     total_price = models.IntegerField()
    


def __str__(self):
       return self.name
  
  