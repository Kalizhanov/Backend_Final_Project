from django import template
from main.models import Presidents

register = template.Library()

@register.simple_tag(name='getp')
def get_posts(filter=None):
    if not filter:
        return Presidents.objects.all()
    else:
        return Presidents.objects.filter(pk=filter)


@register.inclusion_tag('main/list_posts.html')
def show_posts(sort=None):
    if not sort:
        post2 = Presidents.objects.all()
    else:
        post2 = Presidents.objects.order_by(sort)
    return {'post2' : post2}