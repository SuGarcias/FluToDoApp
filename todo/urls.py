from django.urls import path
from . import views

urlpatterns = [
    path('', views.task_list, name='task_list'),
    path('create/', views.create_task, name='create_task'),
    path('edit/<int:task_id>/', views.edit_task, name='edit_task'),  # Agrega esta línea
    path('mark-done/<int:task_id>/', views.mark_task_done, name='mark_task_done'),
    path('tasks/<int:task_id>/mark_pending/', views.mark_task_pending, name='mark_task_pending'),
    path('delete/<int:task_id>/', views.delete_task, name='delete_task'),
]
