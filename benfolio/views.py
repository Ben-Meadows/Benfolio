from django.shortcuts import render
from .models import Project  # Import Project model

def homepage(request):
    """ Renders the homepage with projects """
    return render(request, 'homepage.html')

