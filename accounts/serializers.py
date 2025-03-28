from rest_framework import serializers
from .models import CustomUser


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'email', 'name', 'mobile', 'is_active', 'is_staff', 'created_at']
        read_only_fields = ['is_active', 'is_staff', 'created_at']
