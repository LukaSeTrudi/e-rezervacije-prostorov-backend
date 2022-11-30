from django.db import models

# Create your models here.
from django.contrib.auth.models import User

class Location(models.Model):
    name = models.CharField(max_length=100)

    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)

    owner_id = models.ForeignKey(User, on_delete=models.PROTECT, related_name='locations')

    website_url = models.URLField(max_length=200, blank=True)
    phone_number = models.CharField(max_length=20, blank=True)
    email = models.EmailField(max_length=100, blank=True)

    def __str__(self):
        return self.name

class LocationCourt(models.Model):
    location = models.ForeignKey(Location, on_delete=models.CASCADE, related_name='courts')
    name = models.CharField(max_length=100)
    
    court_types = models.ManyToManyField('CourtType', related_name='court_types')

    def __str__(self):
        return self.name

class CourtType(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name