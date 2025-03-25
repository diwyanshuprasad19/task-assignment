from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Task
from .serializers import TaskSerializer
from .services import TaskService
from accounts.models import CustomUser
from .exceptions import TaskNotFoundException, UserNotFoundException
from rest_framework.permissions import AllowAny


class TaskCreateView(APIView):
    permission_classes = [AllowAny]  # No authentication required

    def post(self, request):
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            task = TaskService.create_task(serializer.validated_data)
            return Response({'message': 'Task created successfully', 'task_id': task.id}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TaskAssignView(APIView):
    permission_classes = [AllowAny]  # No authentication required

    def post(self, request, task_id):
        try:
            task = Task.objects.get(pk=task_id)
            user_ids = request.data.get('user_ids', [])
            users = CustomUser.objects.filter(id__in=user_ids)
            TaskService.assign_task(task, users)
            return Response({'message': 'Task assigned successfully'}, status=status.HTTP_200_OK)
        except Task.DoesNotExist:
            raise TaskNotFoundException


class AccountTasksView(APIView):
    permission_classes = [AllowAny]  # No authentication required

    def get(self, request, account_id):
        try:
            user = CustomUser.objects.get(pk=account_id)
            tasks = TaskService.get_user_tasks(user)
            serializer = TaskSerializer(tasks, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except CustomUser.DoesNotExist:
            raise UserNotFoundException
