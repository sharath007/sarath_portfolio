from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Project
from .resources import ProjectResource
from django.contrib import messages
from tablib import Dataset
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateNewUser
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

# Create your views here.
# portfolio app
#---------------------------------
def home(request):
    projects = Project.objects.all()
    return render(request,'portfolio/home.html',{'projects':projects})
#-------------------------------
def registerpage(request):
    if request.method == 'POST':
        form = CreateNewUser(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request,'Successfully Registered for ' + user)

            return redirect('login')
    else:
        form = CreateNewUser()

    return render(request,'portfolio/register.html',{'form': form})
#---------------------------------
def loginpage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            messages.info(request,'Username or Password is incorrect')
    context = {}
    return render(request,'portfolio/login.html',context)
#---------------------------------
def aboutus(request):
    return render(request,'portfolio/aboutus.html')
#---------------------------------
def managesite(request):
    return render(request,'portfolio/SiteManagement.html')
#---------------------------------
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
#---------------------------------
