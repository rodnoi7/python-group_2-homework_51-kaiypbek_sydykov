from django.shortcuts import render, redirect, get_object_or_404
from to_do_list.forms import TaskForm
from to_do_list.models import Task
from django.views.generic import View

# Create your views here.

class IndexView(View):
    def get(self, request, *args, **kwargs):
        form = TaskForm()
        tasks = Task.objects.all()
        context = {
            'tasks': tasks,
            'form': form
        }
        return render(request, 'index.html', context)

def create_view(request):
    if request.method == 'POST':
        form = TaskForm(data=request.POST)
        if form.is_valid():
            task = Task.objects.create(
                name=form.cleaned_data['name'],
                status=form.cleaned_data['status']
            )
            return redirect('index')
        else:
            form = TaskForm()
            tasks = Task.objects.all()
            context = {
                'tasks': tasks,
                'form': form
            }
            return render(request, 'index.html', context)

def update_view(request, task_pk):
    task = get_object_or_404(Task, pk=task_pk)
    if task.status == 'Новая':
        task.status = 'В процессе'
    elif task.status == 'В процессе':
        task.status = 'Завершено'
    task.save()
    return redirect('index')

def delete_view(request, task_pk):
    task = get_object_or_404(Task, pk=task_pk)
    if request.method == 'GET':
        return render(request, 'delete_task.html', context={"task":task})
    elif request.method == 'POST':
        if request.POST.get('delete') == 'yes':
            task.delete()
        return redirect('index')

def delete_finished_tasks(request):
    if request.method == 'GET':
        tasks = Task.objects.filter(status='Завершено')
        context = {
            'tasks': tasks
        }
        return render(request, 'delete_fin_tasks.html', context)
    elif request.method == 'POST':
        if request.POST.get('delete') == 'yes':
            tasks = Task.objects.filter(status='Завершено')
            tasks.delete()
        return redirect('index')