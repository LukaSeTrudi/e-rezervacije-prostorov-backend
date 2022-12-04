from django.contrib import admin
from apps.profiles.models import UserProfile
# Register your models here.

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'full_name', 'is_company', 'is_active']

admin.site.register(UserProfile, UserProfileAdmin)