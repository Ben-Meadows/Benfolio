from django.shortcuts import render, get_object_or_404
from .models import Project  # Import Project model
from django.conf import settings
from django.core.mail import send_mail, BadHeaderError
from django.contrib import messages
from django.http import HttpResponse

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
    if request.method == 'POST':
        name = request.POST.get('name', '').strip()
        email = request.POST.get('email', '').strip()
        subject = request.POST.get('subject', '').strip()
        message = request.POST.get('message', '').strip()

        if not (name and email and subject and message):
            messages.error(request, 'Please fill in all fields.')
        else:
            body = f"From: {name} <{email}>\n\n{message}"
            try:
                send_mail(
                    subject=f"Portfolio contact: {subject}",
                    message=body,
                    from_email=settings.DEFAULT_FROM_EMAIL,
                    recipient_list=[settings.CONTACT_EMAIL],
                    fail_silently=False,
                )
                messages.success(request, 'Thanks! Your message has been sent.')
            except BadHeaderError:
                messages.error(request, 'Invalid header found.')
            except Exception:
                messages.error(request, 'Sorry, something went wrong sending your message.')

    return render(request, 'contact.html')


def healthz(request):
    """Lightweight health check endpoint for uptime monitoring."""
    return HttpResponse("ok", content_type="text/plain")
