from django.db import models
from django.utils import timezone

from django.utils.html import mark_safe
from datetime import datetime
import os, random

now = timezone.now

def image_path(instance, filename):
    basefilename, file_extension = os.path.splitext(filename)
    chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890'
    randomstr = ''.join((random.choice(chars)) for x in range(10))
    _now = datetime.now()
    return (f"service_pic/{_now.strftime('%Y')}-{_now.strftime('%m')}-{instance}-{basefilename}-{randomstr}{file_extension}")

def image_path_project(instance, filename):
    basefilename, file_extension = os.path.splitext(filename)
    chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890'
    randomstr = ''.join((random.choice(chars)) for x in range(10))
    _now = datetime.now()
    return (f"project_pic/{_now.strftime('%Y')}-{_now.strftime('%m')}-{instance}-{basefilename}-{randomstr}{file_extension}")

def image_path_event(instance, filename):
    basefilename, file_extension = os.path.splitext(filename)
    chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890'
    randomstr = ''.join((random.choice(chars)) for x in range(10))
    _now = datetime.now()
    return (f"event_pic/{_now.strftime('%Y')}-{_now.strftime('%m')}-{instance}-{basefilename}-{randomstr}{file_extension}")

class Experience(models.Model):
    company_name = models.CharField(max_length=200, verbose_name='Company Name')
    position = models.CharField(max_length=200, verbose_name='Position')
    date_hired = models.DateField(default=now)

    def __str__(self):
        return self.company_name

class Skill(models.Model):
    skill_name = models.CharField(max_length=200, verbose_name='Skill')

    def __str__(self):
        return self.skill_name

class Service(models.Model):
    service_name = models.CharField(max_length=200, verbose_name='Service')
    service_description = models.TextField(verbose_name='Description')
    service_image = models.ImageField(upload_to=image_path, default='service_pic/default.png')

    def __str__(self):
        return self.service_name
    
    def image_tag(self):
        return mark_safe(f'<img src="/media/{self.service_image}" width="300" height="300"/>')

class Project(models.Model):
    project_name = models.CharField(max_length=200, verbose_name='Project Name')
    client_name = models.CharField(max_length=200, verbose_name='Client Name')
    project_description = models.TextField(verbose_name='Description')
    project_image = models.ImageField(upload_to=image_path_project, default='project_pic/default.png')

    def __str__(self):
        return self.project_name
    
    def image_tag(self):
        return mark_safe(f'<img src="/media/{self.project_image}" width="300" height="300"/>')

class Event(models.Model):
    event_name = models.CharField(max_length=200, verbose_name='Event Name')
    participants = models.CharField(max_length=200, verbose_name='Participants')
    event_description = models.TextField(verbose_name='Description')
    event_image = models.ImageField(upload_to=image_path_event, default='event_pic/default.png')
    event_date = models.DateField(default=now)

    def __str__(self):
        return self.event_name
    
    def image_tag(self):
        return mark_safe(f'<img src="/media/{self.event_image}" width="300" height="300"/>')