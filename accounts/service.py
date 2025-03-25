from accounts.models import CustomUser  # Importing your Custom User Model
from django.core.exceptions import ValidationError

class UserService:

    @staticmethod
    def create_user(data):
        user = CustomUser.objects.create(
            name=data['name'],
            email=data['email'],
            mobile=data['mobile'],
        )
        return {
            'message': 'User created successfully',
            'user_id': user.id
        }
