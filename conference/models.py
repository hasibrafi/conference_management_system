from django.contrib import admin
from django.db import models 

# Create your models here.

class Conference(models.Model):
    
    type_choices = [
        ('Conference', 'Conference'),
        ('Journal', 'Journal'),
    ]
    
    type = models.CharField(max_length=20, choices=type_choices)
    title = models.CharField(max_length=255)
    acronym = models.CharField(max_length=255)
    web_page = models.URLField(max_length=200)
    city = models.CharField(max_length=100)
    venue = models.CharField(max_length=255)
    country = models.CharField(max_length=100)
    est_submissions = models.IntegerField()
    first_day = models.DateTimeField(auto_now_add=False, null=True)
    last_day = models.DateTimeField(auto_now_add=False, null=True)
    primary_area = models.CharField(max_length=255)
    secondary_area = models.CharField(max_length=250, null=True)
    area_notes = models.CharField(max_length=255)
    organizer = models.CharField(max_length=100)
    organizer_webpage = models.URLField(max_length=200)
    
    def __str__(self):
        return self.title