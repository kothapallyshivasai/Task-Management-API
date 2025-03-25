from django.urls import path
from .views import create_task, assign_task, list_tasks, list_users, user_tasks, register_user

urlpatterns = [
    path('tasks/create/', create_task, name='create_task'),   
    path('tasks/<int:task_id>/assign/', assign_task, name='assign_task'),  
    path('users/<int:user_id>/tasks/', user_tasks, name='user_tasks'),   
    path('register/', register_user, name='register_user'),
    path('users/', list_users, name='list_users'),
    path('tasks/', list_tasks, name='list_tasks'),
]
