from django.shortcuts import render
from .models import Project  # Import Project model

def homepage(request):
    """ Renders the homepage with projects """
    projects = Project.objects.order_by('-project_date_start', '-created_at')
    context = {
        'projects': projects
    }

    
    
    return render(request, 'homepage.html', context)
