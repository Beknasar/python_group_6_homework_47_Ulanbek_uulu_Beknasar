from django.shortcuts import render,redirect, get_object_or_404
from webapp.models import Tasks, STATUS_CHOICES
from django.http import HttpResponseNotAllowed


def index_view(request):
    data = Tasks.objects.all()
    return render(request, 'index.html', context={'tasks': data})

def task_view(request, pk):
    task = get_object_or_404(Tasks, pk=pk)
    context = {'task': task}
    return render(request, 'task_view.html', context)

def create_task_view(request):
    if request.method == 'GET':
        return render(request, 'task_create.html', context={
            'status_choices': STATUS_CHOICES
        })
    elif request.method == 'POST':
        #print(request.POST)
        title = request.POST.get('title')
        description = request.POST.get('description')
        status = request.POST.get('status')
        date = request.POST.get('date')
        if date == '':
            date = None
        task = Tasks.objects.create(description=description, status=status, title=title, task_deadline=date)

        return redirect('task_view', pk=task.pk)
    else:
        return HttpResponseNotAllowed(
            permitted_methods=['GET', 'POST'])

def update_view(request, pk):
    task = get_object_or_404(Tasks, pk=pk)
    if request.method == "GET":
        return render(request, 'task_update.html', context={
            'status_choices': STATUS_CHOICES,
            'task': task
        })
    elif request.method == "POST":
        errors = {}
        task.title = request.POST.get('title')
        if not task.title:
            errors['title'] = 'This field is required!'
        task.description = request.POST.get('description')
        if not task.description:
            errors['description'] = 'This field is required!'
        task.status = request.POST.get('status')
        task.date = request.POST.get('date')

        if errors:
            return render(request, 'task_update.html', context={
                'status_choices': STATUS_CHOICES,
                'task': task,
                'errors': errors
            })
        task.save()
        return redirect('task_view', pk=task.pk)
    else:
        return HttpResponseNotAllowed(permitted_methods=['GET', 'POST'])

def delete_view(request, pk):
    task = get_object_or_404(Tasks, pk=pk)
    if request.method == 'GET':
        return render(request, 'task_delete.html', context={'task': task})
    elif request.method == 'POST':
        task.delete()
        return redirect('index')