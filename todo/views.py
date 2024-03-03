# views.py
from django.shortcuts import render, redirect, get_object_or_404
from .models import Task
from .forms import TaskForm
from django.db.models import Case, Value, When

def task_list(request):
    priority_order = {'HIGH': 1, 'MEDIUM': 2, 'LOW': 3}
    tasks = Task.objects.all().order_by(Case(
        *[When(priority=priority, then=Value(index)) for priority, index in priority_order.items()]
    ))
    return render(request, 'task_list.html', {'tasks': tasks})

def create_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = TaskForm()
    return render(request, 'create_task.html', {'form': form})

def edit_task(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = TaskForm(instance=task)
    return render(request, 'edit_task.html', {'form': form})


def toggle_task(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    task.done = not task.done  
    task.save()
    return redirect('task_list')


def delete_task(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    task.delete()
    return redirect('task_list')
