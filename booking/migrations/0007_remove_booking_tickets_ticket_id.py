# Generated by Django 3.0.4 on 2020-04-30 08:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0006_auto_20200430_1406'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking_tickets',
            name='ticket_id',
        ),
    ]
