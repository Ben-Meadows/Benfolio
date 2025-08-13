from django.urls import path
from . import views
from .views import homepage, project_detail, projects

urlpatterns = [
    path('', homepage, name='homepage'),
    path('projects/', projects, name='projects'),
    path('projects/<slug:slug>/', project_detail, name='project_detail'),
]
