from import_export import resources
from .models import Project

class ProjectResource(resources.ModelResource):
    class meta:
        model = Project
