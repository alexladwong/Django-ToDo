from django.shortcuts import render
from app_todo.models import *


def home(request):
    task = Task.objects.filter(is_completed=False)
    context = {
        "tasks": task, 
        }
    return render(request, "home.html", context)
    