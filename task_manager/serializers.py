from rest_framework import serializers
from .models import Task, Project
from django.contrib.auth import get_user_model

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ['owner']


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'
        read_only_fields = ['owner']


User = get_user_model()
class RegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password', 'email')
    
    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
            email=validated_data['email']
        )
        return user

