from rest_framework.exceptions import APIException


class TaskManagementException(APIException):
    status_code = 400
    default_detail = 'A task management error occurred.'
    default_code = 'task_management_error'


class InvalidStatusException(TaskManagementException):
    default_detail = 'The provided status is invalid.'
    default_code = 'invalid_status'


class TaskNotFoundException(TaskManagementException):
    default_detail = 'The requested task was not found.'
    default_code = 'task_not_found'


class UserNotFoundException(TaskManagementException):
    default_detail = 'The requested user was not found.'
    default_code = 'user_not_found'
