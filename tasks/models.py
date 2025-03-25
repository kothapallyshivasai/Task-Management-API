from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission

# Django provides a default User model with essential fields, we extend it to add a mobile field.
class User(AbstractUser):
    mobile = models.CharField(max_length=15, unique=True)

    # Permissions for the AbstractUser to work
    groups = models.ManyToManyField(Group, related_name="custom_user_groups", blank=True)
    user_permissions = models.ManyToManyField(Permission, related_name="custom_user_permissions", blank=True)

class Task(models.Model):

    name = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    assigned_users = models.ManyToManyField(User, related_name='tasks')

    def __str__(self):
        return self.name
