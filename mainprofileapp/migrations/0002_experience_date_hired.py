# Generated by Django 3.2 on 2021-04-27 04:27

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('mainprofileapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='experience',
            name='date_hired',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
