from django.urls import path
from .views import TaskCreateView, TaskAssignView, AccountTasksView

urlpatterns = [
    path('create/', TaskCreateView.as_view(), name='create_task'),
    path('<int:task_id>/assign/', TaskAssignView.as_view(), name='assign_task'),
    path('tasks/', AccountTasksView.as_view(), name='user_tasks'),
]
