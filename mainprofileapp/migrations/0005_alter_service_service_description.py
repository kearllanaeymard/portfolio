# Generated by Django 3.2 on 2021-04-27 04:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainprofileapp', '0004_service'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='service_description',
            field=models.TextField(verbose_name='Description'),
        ),
    ]
