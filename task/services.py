from .models import Task
from .exceptions import InvalidStatusException, TaskNotFoundException, UserNotFoundException
from accounts.models import CustomUser
from .constants import TASK_STATUSES


class TaskService:

    @staticmethod
    def validate_status(status):
        if status not in TASK_STATUSES:
            raise InvalidStatusException

    @staticmethod
    def create_task(validated_data):
        # Validate the status if provided
        if 'status' in validated_data:
            TaskService.validate_status(validated_data['status'])

        task = Task.objects.create(
            name=validated_data['name'],
            description=validated_data['description'],
            task_type=validated_data.get('task_type', 'General'),
            status=validated_data.get('status', 'PENDING')
        )
        return task

    @staticmethod
    def assign_task(task, users):
        if not users.exists():
            raise UserNotFoundException("No valid users found to assign the task.")
        task.assigned_users.set(users)
        task.save()

    @staticmethod
    def get_user_tasks(user):
        if not user:
            raise UserNotFoundException("User not found.")
        return Task.objects.filter(assigned_users=user)
