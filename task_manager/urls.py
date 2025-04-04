from django.urls import path
from .views import TaskCreateView, TaskDetailView, TaskUpdateView, TaskDeleteView, TaskListView, ProjectListView, ProjectRetrieveView, ProjectUpdateView, ProjectDestroyView

urlpatterns = [
    path('tasks/', TaskListView.as_view(), name='task-list'),
    path('tasks/create/', TaskCreateView.as_view(), name='task-create'),
    path('tasks/<int:pk>/', TaskDetailView.as_view(), name='task-detail'),
    path('tasks/<int:pk>/update/', TaskUpdateView.as_view(), name='task-update'),
    path('tasks/<int:pk>/delete/', TaskDeleteView.as_view(), name='task-delete'),

    path('projects/', ProjectListView.as_view(), name='project-list'),
    path('projects/create/', ProjectListView.as_view(), name='project-create'),
    path('projects/<int:pk>/', ProjectRetrieveView.as_view(), name='project-detail'),
    path('projects/<int:pk>/update/', ProjectUpdateView.as_view(), name='project-update'),
    path('projects/<int:pk>/delete/', ProjectDestroyView.as_view(), name='project-delete'),
]