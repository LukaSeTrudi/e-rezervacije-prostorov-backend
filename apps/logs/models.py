from django.db import models

# Create your models here.

class Log(models.Model):
    LOG_TYPE_USER_PROFILE_SHOWN = 'user_shown'
    LOG_TYPE_USER_PROFILE_DETAIL = 'user_detail'

    LOG_TYPE_LOCATION_SHOWN = 'location_shown'
    LOG_TYPE_LOCATION_DETAIL = 'location_detail'
    
    LOG_TYPE_COURT_SHOWN = 'court_shown'
    LOG_TYPE_COURT_DETAIL = 'court_detail'

    LOG_TYPES = (
        (LOG_TYPE_USER_PROFILE_SHOWN, 'User profile shown'),
        (LOG_TYPE_USER_PROFILE_DETAIL, 'User profile detail'),
        (LOG_TYPE_LOCATION_SHOWN, 'Location shown'),
        (LOG_TYPE_LOCATION_DETAIL, 'Location detail'),
        (LOG_TYPE_COURT_SHOWN, 'Court shown'),
        (LOG_TYPE_COURT_DETAIL, 'Court detail'),
    )

    user = models.ForeignKey('auth.User', on_delete=models.SET_NULL, null=True, related_name='logs')
    created_at = models.DateTimeField(auto_now_add=True)
    
    location = models.ForeignKey('locations.Location', on_delete=models.SET_NULL, null=True)
    court = models.ForeignKey('locations.LocationCourt', on_delete=models.SET_NULL, null=True)
    user_profile = models.ForeignKey('profiles.UserProfile', on_delete=models.SET_NULL, null=True)

    log_type = models.CharField(max_length=100, choices=LOG_TYPES)

    def __str__(self):
        return f'{self.user} - {self.log_type} - {self.created_at} '