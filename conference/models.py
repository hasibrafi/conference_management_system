from django.db.models.deletion import CASCADE
from django.contrib import admin
from django.db import models 

# Create your models here.

class Conference(models.Model):
    
    Types = [
        ('Conference', 'Conference'),
        ('Journal', 'Journal'),
        ('Book', 'Book'),
    ] 

    CITY = [
        ('Amsterdam','Amsterdam'), ('Bengalore','Bengalore'), ('California','California'), ('Chattogram','Chattogram'), 
        ('Dhaka',''), ('Delhi','Delhi'), ('Edmonton','Edmonton'), ('Firozabad','Firozabad'), ('Greenville','Greenville'),
        ('Ho Chi Minh City','Ho Chi Minh City'), ('Ibiza','Ibiza'), ('Jessore','Jessore'), ('Kualalampur','Kualalampur'), 
        ('Melbourne','Melbourne'), ('New York','New York'), ('Oslo','Oslo'), 
    ]

    COUNTRY = [
        ('Australia','Australia'), ('Algeria','Algeria'), ('Bangladesh','Bangladesh'), ('Canada','Canada'), 
        ('Denmark','Denmark'), ('England','England'), ('France','France'), ('Germany','Germany'),
        ('Hungary','Hungary'), ('Italy','Italy'), ('Japan','Japan'), ('Kenya','Kenya'),
        ('Luxemburg','Luxemburg'), ('Mexico','Mexico'), ('Norway','Norway'), ('Oman','Oman'),
    ]
    
    AREAS = [
        ('Human Computer Interaction', 'Human Computer Interaction'),
        ('Gamification','Gamification'),
        ('Emerging Technologies','Emerging Technologies'),
        ('Media','Media'),
        ('Communication Networks','Communication Networks'),
        ('Mobile Computing','Mobile Computing'),
        ('Discourse Analysis','Discourse Analysis'),
        ('STEM Education','STEM Education'),
        ('Artificial Intelligence','Artificial Intelligence'),
        ('Robotics','Robotics'),
        ('Microbiology', 'Microbiology'),
        ('Biochemistry','Biochemistry'),
        ('Mechanic Automation','Mechanic Automation'),
        ('Green Energy','Green Energy'),
        ('Environmental Science','Environmental Science'),
        ('Supply Chain System','Supply Chain System'),
        ('Business Strategy','Business Strategy'),
        ('Literature','Literature'),
        ('Art & Music','Art & Music'),
        ('World Peace & Governance','World Peace & Governance'),
    ]

    type = models.CharField(max_length=20, choices=Types)
    title = models.CharField(max_length=255)
    acronym = models.CharField(max_length=255)
    web_page = models.URLField(max_length=200)
    city = models.CharField(max_length=100, choices=CITY)
    venue = models.CharField(max_length=255)
    country = models.CharField(max_length=100, choices=COUNTRY)
    est_submissions = models.IntegerField()
    first_day = models.DateTimeField(auto_now_add=False, null=True)
    last_day = models.DateTimeField(auto_now_add=False, null=True)
    primary_area = models.CharField(max_length=255, choices=AREAS)
    secondary_area = models.CharField(max_length=250, null=True, choices=AREAS)
    area_notes = models.CharField(max_length=255)
    organizer = models.CharField(max_length=100)
    organizer_webpage = models.URLField(max_length=200)
    
    def __str__(self):
        return self.title

class AbstractPaper(models.Model):
    conference = models.ForeignKey(Conference, null=True, on_delete=CASCADE)
    author_name = models.CharField(max_length=100)
    paper_title = models.CharField(max_length=255)
    abstract_file = models.FileField(upload_to='uploads/')

    def __str__(self):
        return self.paper_title