from django.contrib import admin
from apps.logs.models import Log
# Register your models here.

class LogAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'log_type', 'created_at', 'user']

admin.site.register(Log, LogAdmin)