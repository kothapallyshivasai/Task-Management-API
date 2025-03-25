from rest_framework import serializers
from .models import User, Task

# Serializes the User model for API Transfers, including id, username, email, and mobile fields.
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'mobile']

# Serializes the Task model and includes assigned users as nested user data.
class TaskSerializer(serializers.ModelSerializer):
    assigned_users = UserSerializer(many=True, read_only=True)
    class Meta:
        model = Task
        fields = '__all__'

# Allows assigning users to a task using their id's or primary keys.
class AssignTaskSerializer(serializers.ModelSerializer):
    assigned_users = serializers.PrimaryKeyRelatedField(many=True, queryset=User.objects.all())
    class Meta:
        model = Task
        fields = ['assigned_users']
