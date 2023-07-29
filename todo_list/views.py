from django.shortcuts import render, redirect, get_object_or_404
from .models import *

def index(request):
    context = {}
    context['tasks'] = Task.objects.all().order_by('completed', 'id')
    return render(request, 'pages/index.html', context=context)

def addTask(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        new_task = Task.objects.create(
            title=title
        )
    return redirect('index')

def removeTask(request, taskId):
    task = get_object_or_404(Task, id=taskId)
    task.delete()
    return redirect('index')

def changeStatus(request, taskId):
    task = get_object_or_404(Task, id=taskId)
    if task.completed:
        task.completed = False
    else:
        task.completed = True
    task.save()
    return redirect('index')