# Generated by Django 5.1.6 on 2025-06-08 20:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('benfolio', '0002_project_link_project_project_date_end_project_skills'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='project_date_start',
            field=models.DateField(blank=True, help_text='Date you started the project', null=True),
        ),
    ]
