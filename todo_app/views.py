from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.views.generic import ListView, CreateView

from todo_app.services import TaskService
from .models import Task

class TaskListView(View):
    def get(self, request):
        tasks = TaskService.list_tasks()
        return render(request, 'tasks/list.html', {'tasks': tasks})
    def post(self, request):
        data = {
            'title': request.POST.get('title'),
            'due_date': request.POST.get('due_date') or None,
            'priority': request.POST.get('priority'),
            'status': request.POST.get('status'),
        }
        TaskService.add_task(data)
        return redirect('/')

class TaskCreateView(View):
    def post(self, request):
        TaskService.add_task({
            'title': request.POST['title'],
            'due_date': request.POST['due_date'],
            'priority': request.POST['priority'],
            'status': request.POST['status'],
        })
        return redirect('/')

    def get(self, request):
        return render(request, 'tasks/form.html')
    
class TaskMarkDoneView(View):
    def post(self, request, task_id):
        task = get_object_or_404(Task, id=task_id)
        task.status = 'Done'
        task.save()
        TaskService.invalidate_cache()
        return redirect('/')

