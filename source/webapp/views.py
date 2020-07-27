from django.shortcuts import render,redirect, get_object_or_404
from webapp.models import Tasks, STATUS_CHOICES
from django.http import HttpResponseNotAllowed


def index_view(request):
    data = Tasks.objects.all()
    return render(request, 'index.html', context = {'tasks': data})

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
        task = Tasks.objects.create(description=description,
                                    status=status,
                                    title=title,
                                    task_deadline=date)
        return redirect(f'/tasks/{task.pk}/')
    else:
        return HttpResponseNotAllowed(
            permitted_methods=['GET', 'POST'])

def delete_view(request):
    if request.method == 'GET':
        return render(request, 'task_delete.html')
    elif request.method == 'POST':
        task_id = request.POST.get('delete')
        task = Tasks.objects.get(pk=task_id)
        task.delete()
        return redirect('/')