from django.shortcuts import render, redirect, get_object_or_404
from .models import Task
from .forms import TaskForm
# Create your views here.

def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'todo/task_list.html', {'tasks': tasks})

def create_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = TaskForm()
    return render(request, 'todo/create_task.html', {'form': form})

def mark_task_done(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    task.done = True
    task.save()
    return redirect('task_list')

def delete_task(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    task.delete()
    return redirect('task_list')
