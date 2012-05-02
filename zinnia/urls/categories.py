"""Urls for the Zinnia categories"""
from django.conf.urls.defaults import url
from django.conf.urls.defaults import patterns

from zinnia.models import Category
from zinnia.views.decorators import template_name_current_site

category_conf = {'queryset': Category.published.on_site(), 'template_name': template_name_current_site('category_list.html') }

urlpatterns = patterns('django.views.generic.list_detail',
                       url(r'^$', 'object_list',
                           category_conf, 'zinnia_category_list'),
                       )

urlpatterns += patterns('zinnia.views.categories',
                        url(r'^(?P<path>[-\/\w]+)/page/(?P<page>\d+)/$',
                            'category_detail',
                            name='zinnia_category_detail_paginated'),
                        url(r'^(?P<path>[-\/\w]+)/$', 'category_detail',
                            name='zinnia_category_detail'),
                        )
