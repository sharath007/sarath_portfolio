from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import Project

# Register your models here.
admin.site.register(Project)

class ProjectAdmin(ImportExportModelAdmin):
    list_display = ('title','description','image','url')
