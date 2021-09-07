from django.shortcuts import render

# Create your views here.
from my_projects.models import Project

def project_index(request):
    my_projects = Project.objects.all()    # query - command that allows to create,retrieve,update or delete objects(rows) in database
    context = {     # dictionary
        'my_projects' : my_projects
    }
    return render(request, 'project_index.html', context)

def project_detail(request, pk):
    project = Project.objects.get(pk=pk)
    context = {
        'project' : project
    }
    return render(request, 'project_detail.html', context)