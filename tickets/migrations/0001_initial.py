# Generated by Django 3.0.4 on 2020-05-14 09:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ticket_home',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('img', models.ImageField(upload_to='pics')),
                ('date', models.DateField()),
                ('location', models.CharField(max_length=100)),
                ('fullName', models.CharField(max_length=100)),
                ('m_no', models.IntegerField()),
                ('start_time', models.TimeField()),
            ],
        ),
    ]