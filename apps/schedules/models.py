from django.db import models

# Create your models here.

class CourtSchedule(models.Model):
    
    court = models.ForeignKey('locations.LocationCourt', on_delete=models.CASCADE, related_name='schedules')
    day = models.IntegerField()

    start_time = models.TimeField()
    end_time = models.TimeField()

    price = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return self.court.name

class CourtScheduleException(models.Model):
    schedule = models.ForeignKey(CourtSchedule, on_delete=models.CASCADE, related_name='exceptions')
    
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()

    price = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return self.schedule.court.name

class CourtReservation(models.Model):
    schedule = models.ForeignKey(CourtSchedule, on_delete=models.CASCADE, related_name='reservations')
    user = models.ForeignKey('profiles.UserProfile', on_delete=models.CASCADE, related_name='reservations')

    date = models.DateField()

    def __str__(self):
        return self.schedule.court.name