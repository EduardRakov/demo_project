from django.contrib import admin
from demo_project.tasks_manager.models import Project, Task

admin.site.register(Project)
admin.site.register(Task)
