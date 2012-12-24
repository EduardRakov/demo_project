from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from demo_project.tasks_manager.models import Project, Task

def index(request):
    projects = Project.objects.all()
    project = projects[0]
    tasks = Task.objects.filter(project = projects[0])
    return render_to_response('index.html', {'projects' : projects, 'project' : project, 'tasks' : tasks})


@csrf_exempt
def show_projects(request):
    projects = Project.objects.all()
    return render_to_response('projects.html', {'projects' : projects})


@csrf_exempt
def current_project(request):
    project_id = request.POST['project_id']
    project = Project.objects.get(pk = project_id)
    tasks = Task.objects.filter(project = project_id)
    return render_to_response('center_pane.html', {'project' : project, 'tasks' : tasks})


@csrf_exempt
def create_project(request):
    Project.objects.create(name = 'Unnamed Project')
    return HttpResponseRedirect('/tasks_manager/show_projects')


@csrf_exempt
def edit_project(request, project_id):
    Project.objects.filter(pk = project_id).update(name = request.POST['project_name'])
    return HttpResponseRedirect('/tasks_manager/show_projects')



@csrf_exempt
def create_task(request, project_id):
    Task.objects.create(name = '', project =  Project.objects.get(id = project_id))
    tasks = Task.objects.filter(project = project_id)
    return render_to_response('tasks.html', {'tasks' : tasks})


@csrf_exempt
def edit_task(request, task_id):
    Task.objects.filter(pk = task_id).update(name = request.POST['task_name'])
    return HttpResponseRedirect('/tasks_manager/index')