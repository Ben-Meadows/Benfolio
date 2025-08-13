from django.contrib import admin
from .models import Project

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
	list_display = ("title", "project_date_start", "project_date_end", "show_on_home", "created_at")
	list_filter = ("show_on_home",)
	search_fields = ("title", "description", "skills")
	prepopulated_fields = {"slug": ("title",)}
