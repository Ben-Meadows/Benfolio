from django.shortcuts import render, get_object_or_404
from .models import Project  # Import Project model

def homepage(request):
    """ Renders the homepage with projects """
    projects = Project.objects.order_by('-project_date_start', '-created_at')
    context = {
        'projects': projects
    }

    return render(request, 'homepage.html', context)


def project_detail(request, slug):
    project = get_object_or_404(Project, slug=slug)
    return render(request, 'project_detail.html', { 'project': project })


def projects(request):
    """Dedicated projects index page showing all projects as flip cards"""
    projects = Project.objects.order_by('-project_date_start', '-created_at')
    return render(request, 'projects.html', { 'projects': projects })


def contact(request):
    """Contact page with modern form design"""
    return render(request, 'contact.html')
