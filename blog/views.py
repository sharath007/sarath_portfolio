from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Blog
from django.contrib.auth.decorators import login_required
# blog app
# Create your views here.
@login_required(login_url='login')
def all_blogs(request):
    blogs = Blog.objects.all()
    return render(request,'blog/all_blogs.html',{'blogs':blogs})

def detail(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    return render(request,'blog/detail.html',{'blog':blog})
