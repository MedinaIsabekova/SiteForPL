from django.shortcuts import render
from .models import Task
from .forms import TaskForm

def index(request):
    return render(request, 'main/index.html')


def about(request):
    tasks = Task.objects.order_by('-id')
    return render(request, 'main/about.html', {'title': 'About our plans after Finals', 'tasks': tasks})


def kpop(request):
    return render(request, 'main/kpop.html')


def anime(request):
    return render(request, 'main/anime.html')


def create(request):
    form = TaskForm()
    context = {
        'form': form
    }
    return render(request, 'main/create.html')
