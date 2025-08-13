from django.db import models
from django.utils.text import slugify

class Project(models.Model):
    '''table for projects'''
    title = models.CharField(max_length=200)
    description = models.TextField()
    project_date_start  = models.DateField(blank=True,null=True,help_text="Date you started the project")
    project_date_end  = models.DateField(blank=True,null=True,help_text="Date you completed the project")
    skills        = models.CharField(max_length=200,blank=True,help_text="Comma-separated list of skills used")
    link          = models.URLField(blank=True,null=True,help_text="Live URL or repo link (can be empty)")
    image         = models.ImageField(upload_to='projects/', blank=True, null=True)
    slug          = models.SlugField(max_length=220, unique=True, blank=True)
    show_on_home  = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)[:220]
        super().save(*args, **kwargs)