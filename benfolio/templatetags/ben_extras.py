from django import template

register = template.Library()

@register.filter
def split_csv(value):
    """
    Split a comma-separated string into a list of trimmed strings.
    Usage: {{ project.skills|split_csv }}
    """
    if not value:
        return []
    return [item.strip() for item in value.split(',') if item.strip()]
