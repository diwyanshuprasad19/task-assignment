from django.urls import path, include
from .views import UserCreateView

urlpatterns = [
    path('create-user/', UserCreateView.as_view(), name='create_user'),
    path('<int:account_id>/', include('task.urls')),
]
