from rest_framework import serializers
from apps.logs.models import Log

class LogListSerializer(serializers.ModelSerializer):    
    class Meta:
        model = Log
        fields = ('id', 'user', 'log_type', 'created_at', 'location', 'court', 'user_profile')