from django.shortcuts import render
from webapp.models import Tasks

def index_view(request):
    data = Tasks.objects.all()
    return render(request, 'index.html', context = {
        'tasks': data
    })
