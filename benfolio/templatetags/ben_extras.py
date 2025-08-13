from django import template

register = template.Library()


@register.filter(name="split_csv")
def split_csv(value: str):
	"""Split a comma-separated string into a list of trimmed items.

	Usage in template: {{ value|split_csv }} or {% for tag in project.skills|split_csv %}
	"""
	if not value:
		return []
	# Ensure we return only non-empty trimmed tokens
	return [item.strip() for item in str(value).split(',') if item.strip()]

