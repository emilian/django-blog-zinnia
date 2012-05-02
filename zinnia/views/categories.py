"""Views for Zinnia categories"""
from django.shortcuts import get_object_or_404
from django.views.generic.list_detail import object_list

from zinnia.models import Category
from zinnia.views.decorators import template_name_current_site


def get_category_or_404(path):
    """Retrieve a Category by a path"""
    path_bits = [p for p in path.split('/') if p]
    return get_object_or_404(Category, slug=path_bits[-1])


def category_detail(request, path, page=None, **kwargs):
    """Display the entries of a category"""
    extra_context = kwargs.pop('extra_context', {})

    category = get_category_or_404(path)
    if not kwargs.get('template_name'):
        kwargs['template_name'] = template_name_current_site('entry_list.html')

    extra_context.update({'category': category})
    kwargs['extra_context'] = extra_context

    assert False, kwargs

    return object_list(request, queryset=category.entries_published(),
                       **kwargs)
