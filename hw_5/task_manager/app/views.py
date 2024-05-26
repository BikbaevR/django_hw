from django.shortcuts import render, get_object_or_404, redirect
from .models import Task


# Create your views here.


def index(request):
    tasks = Task.objects.all()

    cntx = {
        'tasks': tasks
    }
    return render(request, 'app/index.html', context=cntx)


def done(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    task.is_done = True
    task.save()
    return redirect('index')


def un_done(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    task.is_done = False
    task.save()
    return redirect('index')


def delete(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    print(task)
    task.delete()
    return redirect('index')
