from apps.locations.models import CourtType, Location
from rest_framework import serializers

class LocationListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ('id', 'name')

class LocationDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ('id', 'name', 'latitude', 'longitude', 'website_url', 'phone_number', 'email')

class CourtTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourtType
        fields = ('id', 'name')