# Generated by Django 3.0.4 on 2020-06-11 13:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='print_tickets',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('matchfullname', models.CharField(max_length=50)),
                ('gate', models.IntegerField()),
                ('seat_numbers', models.CharField(max_length=20)),
                ('match_number', models.IntegerField()),
                ('match_time', models.TimeField()),
                ('location', models.CharField(max_length=50)),
                ('match_image', models.ImageField(upload_to='')),
            ],
        ),
    ]
