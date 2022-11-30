from apps.locations.models import Location
from rest_framework import serializers

class LocationCreateSerializer(serializers.ModelSerializer):
    owner_id = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = Location
        fields = ('name', 'latitude', 'longitude', 'owner_id', 'website_url', 'phone_number', 'phone_number', 'email')

class LocationListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ('id', 'name')

class LocationDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ('id', 'name', 'latitude', 'longitude', 'website_url', 'phone_number', 'phone_number', 'email')