#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
import random

from django.http import Http404, HttpResponse
from django.shortcuts import render_to_response
from django.conf import settings

from core.models import Content


def view_content(request, **kwargs):
    """Builds Index page."""
    template = kwargs.get('template', None)
    section = kwargs.get('section', None)
    if (not template) or (not section):
        raise Http404
    template = '.'.join([template, 'html'])
    data = Content.objects \
      .filter(section__label=section, section__is_active=True) \
      .order_by('order_id')
    page_img = data[0].section.bg_image + ".jpg"
    return render_to_response(template, {
        'page_title': get_page_title(section),
        'content': [list(data)],
        'menu': get_menu(),
        'page_img': page_img,
        'static_url': settings.STATIC_URL
        })


def get_page_title(lb):
    """Fills page title."""
    if lb:
        return "%s: %s" % (settings.PROJECT_NAME, lb)
    return settings.PROJECT_NAME


def get_menu():
    return [
        {'label': 'index', 'uri': '/'},
        {'label': 'watch', 'uri': '/watch/'},
        {'label': 'listen', 'uri': '/listen/'},
        {'label': 'read', 'uri': '/read/'},
        {'label': 'rider', 'uri': '/rider/'},
        {'label': 'contact', 'uri': '/contact/'},
        ]
