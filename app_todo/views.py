from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render

from .models import Task

# Create your views here.
def addTask(request):
    task = request.POST['task']
    Task.objects.create(task= task)
    return redirect('homepage')

def mark_as_done(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.is_completed = True
    task.save()
    return redirect('homepage')

def incomplete_tasks(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.is_completed = False
    task.save()
    return redirect('homepage')


def edit_task(request, pk):
    get_task = get_object_or_404(Task, pk=pk)
    if request.method == "POST":
        updated_task = request.POST['task']
        get_task.task = updated_task
        get_task.save()
        return redirect('homepage')
    else:
        context = {
            "get_task": get_task,
        }
        return render(request, 'edit_task.html', context)
    
def delete_task(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.delete()
    
    return redirect('homepage')