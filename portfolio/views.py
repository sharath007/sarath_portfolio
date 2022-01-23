from django.shortcuts import render
from django.http import HttpResponse
from .models import Project
from .resources import ProjectResource
from django.contrib import messages
from tablib import Dataset

# Create your views here.
# portfolio app
def home(request):
    projects = Project.objects.all()
    return render(request,'portfolio/home.html',{'projects':projects})

def simple_upload(request):
    if request.method == 'POST':
        project_resource = ProjectResource()
        dataset = Dataset()
        new_project = request.FILES['myfile']

        if not new_project.name.endswith('xlsx'):
            messages.info(request,'wrong format')
            return render(request,'upload.html')

        imported_data = dataset.load(new_project.read(),format='xlsx')
        for data in imported_data:
            value = Project(
                data[0],
                data[1],
                data[2],
                data[3]
                )
            value.save()
    return render(request,'portfolio/upload.html')
