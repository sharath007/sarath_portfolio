"""online_farming URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
#portfolio app
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from portfolio import views
#from projectapp import views

urlpatterns = [
    path('admin/', admin.site.urls, name = 'admincontrol'),
    path('',views.home,name='home'),
    path('blog/', include('blog.urls')),
    path('upload/',views.simple_upload, name = 'Data_Update'),
    path('aboutus/',views.aboutus,name='aboutus'),
    path('login/', views.loginpage, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('register/', views.registerpage,name = 'register'),
    path('managesite/', views.managesite,name = 'managesite'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
