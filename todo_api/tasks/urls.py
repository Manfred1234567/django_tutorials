from django.urls import path
from .views import get_routes, get_tasks, create_task, update_task, delete_task

urlpatterns = [
    path('',get_routes, name='routes'),
    path('api/tasks/',get_tasks, name='tasks'),
    path('api/tasks/create/',create_task, name='create'),
    path('api/tasks/update/<int:pk>/', update_task, name="update"),
    path('api/tasks/delete/<int:pk>/', delete_task, name='delete')
]
