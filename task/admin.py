from django.contrib import admin
from .models import Task
from django.contrib.auth import get_user_model

User = get_user_model()

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'status', 'task_type', 'created_at', 'completed_at', 'assigned_users_list')
    list_filter = ('status', 'created_at', 'task_type')
    search_fields = ('name', 'description')
    ordering = ('-created_at',)
    filter_horizontal = ('assigned_users',)

    def assigned_users_list(self, obj):
        return ", ".join([user.email for user in obj.assigned_users.all()])
    assigned_users_list.short_description = 'Assigned Users'
