from apps.locations.models import LocationCity
from rest_framework import serializers

class LocationCitySerializer(serializers.ModelSerializer):
    class Meta:
        model = LocationCity
        fields = ('id', 'name')