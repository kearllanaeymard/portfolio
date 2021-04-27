# Generated by Django 3.2 on 2021-04-27 16:44

from django.db import migrations, models
import mainprofileapp.models


class Migration(migrations.Migration):

    dependencies = [
        ('mainprofileapp', '0005_alter_service_service_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_name', models.CharField(max_length=200, verbose_name='Project Name')),
                ('client_name', models.CharField(max_length=200, verbose_name='Client Name')),
                ('project_description', models.TextField(verbose_name='Description')),
                ('project_image', models.ImageField(default='project_pic/default.png', upload_to=mainprofileapp.models.image_path_project)),
            ],
        ),
    ]
