from django.urls import path
from . import views


urlpatterns = [
    path('', views.index), #takes you to index page to register and login.
    path('register', views.register), #processes registration
    path('login', views.login),#processes login.
    path('dashboard', views.dashboard),
    path('logout',views.logout), #process logout
    path('jobs/new', views.new_job), #renders add job page
    path('add_job', views.add_job), #adds job to database
    path('jobs/<int:id>', views.job_details),
    path('jobs/edit/<int:id>', views.job_edit),
    path('edit/<int:id>',views.edit), #edits current job
    path('jobs/<int:id>/delete', views.delete),
]