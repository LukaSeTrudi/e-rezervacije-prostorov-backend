from apps.locations.models import Location
from rest_framework import serializers

class LocationCreateSerializer(serializers.ModelSerializer):
    owner = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = Location
        fields = ('name', 'latitude', 'longitude', 'owner', 'website_url', 'phone_number', 'email')

class LocationListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ('id', 'name')

class LocationDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ('id', 'name', 'latitude', 'longitude', 'website_url', 'phone_number', 'email')