# Generated by Django 5.0.1 on 2024-02-28 02:42

import datetime
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CarType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state', models.CharField(choices=[('AB', 'Alberta'), ('BC', 'British Columbia'), ('MB', 'Manitoba'), ('NB', 'New Brunswick'), ('NL', 'Newfoundland and Labrador'), ('NT', 'Northwest Territories'), ('NS', 'Nova Scotia'), ('NU', 'Nunavut'), ('ON', 'Ontario'), ('PE', 'Prince Edward Island'), ('QC', 'Quebec'), ('SK', 'Saskatchewan'), ('YT', 'Yukon')], max_length=100)),
                ('city', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='RegisterDriver',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('phone_number', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=100)),
                ('confirm_password', models.CharField(max_length=100)),
                ('gender', models.CharField(choices=[('male', 'Male'), ('female', 'Female'), ('other', 'Other')], max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Ride',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rider_name', models.CharField(max_length=100)),
                ('rider_email', models.EmailField(max_length=254)),
                ('rider_phone', models.CharField(max_length=20)),
                ('car_name', models.CharField(max_length=100)),
                ('pickup_date', models.DateTimeField(default=datetime.datetime.now)),
                ('drop_off_date', models.DateTimeField(default=datetime.datetime.now)),
                ('price', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('car_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rideapp.cartype')),
                ('from_location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='from_location_rides', to='rideapp.location')),
                ('to_location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='to_location_rides', to='rideapp.location')),
            ],
        ),
    ]
