from django.conf.urls import patterns, include, url
# Uncomment the next two lines to enable the admin:
from django.contrib import admin


admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'demo_project.views.home', name='home'),
    # url(r'^demo_project/', include('demo_project.foo.urls')),
    url(r'^tasks_manager/index$', 'demo_project.tasks_manager.views.index'),
    url(r'^tasks_manager/show_projects', 'demo_project.tasks_manager.views.show_projects'),
    url(r'^tasks_manager/show_tasks', 'demo_project.tasks_manager.views.show_projects'),
    url(r'^tasks_manager/create_project', 'demo_project.tasks_manager.views.create_project'),
    url(r'^tasks_manager/(?P<project_id>\d+)/create_task', 'demo_project.tasks_manager.views.create_task'),
    url(r'^tasks_manager/current_project', 'demo_project.tasks_manager.views.current_project'),
    url(r'^tasks_manager/(?P<project_id>\d+)/edit_project', 'demo_project.tasks_manager.views.edit_project'),
    url(r'^tasks_manager/(?P<task_id>\d+)/edit_task', 'demo_project.tasks_manager.views.edit_task'),
    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
#(?P<project_id>\d+)
#url(r'^***/(?P<person_id>\d+)/save', '***.**.views.****')