from django.urls import path
from .views import TaskListView, TaskCreateView, TaskMarkDoneView

urlpatterns = [
    path('', TaskListView.as_view(), name='task_list'),
    path('add/', TaskCreateView.as_view(), name='task_add'),
    path('done/<int:task_id>/', TaskMarkDoneView.as_view(), name='mark_done'),
]