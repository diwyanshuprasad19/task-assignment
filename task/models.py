from django.db import models
from accounts.models import CustomUser
from .constants import STATUS_CHOICES


class Task(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    task_type = models.CharField(max_length=100)
    completed_at = models.DateTimeField(null=True, blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='PENDING')
    assigned_users = models.ManyToManyField(CustomUser, related_name='tasks')

    def __str__(self):
        return self.name
