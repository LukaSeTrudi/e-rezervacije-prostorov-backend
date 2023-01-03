from django.contrib import admin

from apps.locations.models import CourtType, Location, LocationCourt, LocationCity

from import_export.admin import ImportExportModelAdmin
from import_export import resources
# Register your models here.

class LocationAdmin(admin.ModelAdmin):
    list_display = ['name', 'latitude', 'longitude', 'owner', 'website_url', 'phone_number', 'email']
    search_fields = ['name', 'latitude', 'longitude', 'owner', 'website_url', 'phone_number', 'email']

class LocationCourtAdmin(admin.ModelAdmin):
    list_display = ['location', 'name']
    search_fields = ['location', 'name']

class CourtTypeResource(resources.ModelResource):
    class Meta:
        model = CourtType

class CourtTypeAdmin(ImportExportModelAdmin):
    list_display = ['name']
    search_fields = ['name']
    resource_classes = [CourtTypeResource]

class LocationCityAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']


admin.site.register(Location, LocationAdmin)
admin.site.register(LocationCourt, LocationCourtAdmin)
admin.site.register(CourtType, CourtTypeAdmin)
admin.site.register(LocationCity, LocationCityAdmin)