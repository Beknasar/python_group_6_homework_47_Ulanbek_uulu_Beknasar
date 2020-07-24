from django.shortcuts import render
from webapp.models import Tasks, STATUS_CHOICES
from django.http import HttpResponseNotAllowed
from django.shortcuts import redirect

def index_view(request):
    data = Tasks.objects.all()
    return render(request, 'index.html', context = {
        'tasks': data
    })

def create_task_view(request):
    if request.method == 'GET':
        return render(request, 'task_create.html', context={
            'status_choices': STATUS_CHOICES
        })
    elif request.method == 'POST':
        #print(request.POST)
        description = request.POST.get('description')
        status = request.POST.get('status')
        date = request.POST.get('date')
        if date == '':
            date = None
        task = Tasks.objects.create(description=description,
                                    status=status,
                                    task_deadline=date)
        context = {'task': task}
        return render(request, 'task_view.html', context)
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