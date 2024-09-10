from django.db import models

# Create your models here.
# users/models.py
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    # Add unique related_name to avoid clashes
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='customuser_set',  # Update related_name to avoid conflicts
        blank=True,
        help_text="The groups this user belongs to. A user will get all permissions "
                  "granted to each of their groups.",
        verbose_name="groups",
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='customuser_set',  # Update related_name to avoid conflicts
        blank=True,
        help_text="Specific permissions for this user.",
        verbose_name="user permissions",
    )
