from django.db import models

from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import User
# Create your models here.
from django.utils import timezone

class CourtSchedule(models.Model):
    DAY_OF_WEEK = {
        ('1', 'Monday'),
        ('2', 'Tuesday'),
        ('3', 'Wednesday'),
        ('4', 'Thursday'),
        ('5', 'Friday'),
        ('6', 'Saturday'),
        ('7', 'Sunday'),
    }

    court = models.ForeignKey('locations.LocationCourt', on_delete=models.CASCADE, related_name='schedules')
    day = models.CharField(max_length=1, choices=DAY_OF_WEEK)

    title = models.CharField(max_length=100, blank=True)

    start_time = models.TimeField()
    end_time = models.TimeField()

    price = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)
    
    is_active = models.BooleanField(default=True)
    
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    @property
    def day_formatted(self):
        return self.get_day_display()

    def __str__(self):
        return f'{self.court.location.name} {self.court.name} ({self.day_formatted} {self.start_time} - {self.end_time})' 

class CourtScheduleException(models.Model):
    court = models.ForeignKey('locations.LocationCourt', on_delete=models.CASCADE, related_name='exceptions')
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()

    title = models.CharField(max_length=100, blank=True)

    price = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    is_active = models.BooleanField(default=True)
    reserved_user = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='reserved_courts', null=True)
    
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.court.location.name} {self.court.name} ({self.date} {self.start_time} - {self.end_time})' 

class CourtReservation(models.Model):
    schedule = models.ForeignKey(CourtSchedule, on_delete=models.CASCADE, related_name='reservations')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reservations')

    date = models.DateField()
    confirmed = models.BooleanField(default=False)

    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('schedule', 'date')

    def __str__(self):
        return self.schedule.court.name