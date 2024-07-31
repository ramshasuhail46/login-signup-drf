# Generated by Django 4.2.14 on 2024-07-31 06:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_flight_passenger_seat_reservation'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='otp',
            field=models.IntegerField(default=0, max_length=4),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='status',
            field=models.CharField(choices=[('CONFIRMED', 'Confirmed'), ('PROCESSING', 'Processing'), ('CANCELLED', 'Cancelled')], max_length=20),
        ),
    ]
