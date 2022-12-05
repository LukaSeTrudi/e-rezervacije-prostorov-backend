
from apps.profiles.models import UserProfile
from rest_framework import serializers

class UserListSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(source='user.id')
    username = serializers.CharField(source='user.username')
    email = serializers.CharField(source='user.email')

    class Meta:
        model = UserProfile
        fields = ('id', 'username', 'full_name', 'email', 'is_company', 'bio', 'location', 'avatar')
    

class UserDetailSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(source='user.id')
    username = serializers.CharField(source='user.username')
    email = serializers.CharField(source='user.email')
    
    class Meta:
        model = UserProfile
        fields = ('id', 'username', 'full_name', 'email', 'phone', 'bio', 'location', 'birth_date', 'is_company', 'avatar')
    

class UserUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ('phone', 'bio', 'location', 'birth_date')