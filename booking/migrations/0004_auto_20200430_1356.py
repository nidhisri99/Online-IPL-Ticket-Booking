# Generated by Django 3.0.4 on 2020-04-30 08:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0003_auto_20200430_1355'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking_tickets',
            name='match_date',
            field=models.DateField(default='2020-12-20'),
        ),
    ]
