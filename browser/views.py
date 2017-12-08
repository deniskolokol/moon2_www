#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
import random

from django.http import Http404, HttpResponse
from django.shortcuts import render_to_response
from django.conf import settings

from core.models import Content
from .models import SocialResource, MenuItem


def view_content(request, **kwargs):
    """Outputs specified page."""
    template = kwargs.get('template', None)
    section = kwargs.get('section', None)
    if (not template) or (not section):
        raise Http404

    if not template.endswith('.html'):
        template += '.html'
    data = Content.get_columns(section__label=section, section__is_active=True)
    page_img = data[0][0].section.bg_image + ".jpg"
    if not page_img.endswith('.jpg'):
        page_img += '.jpg'
    return render_to_response(
        template,
        {
            'page_title': get_page_title(section),
            'content': data,

            # XXX add support for tree structure
            'menu': MenuItem.objects.all().order_by('order_id'),
            'social': SocialResource.objects.all().order_by('order_id'),
            'page_img': page_img,
            }
        )


def view_static(request, **kwargs):
    """Outputs static page."""
    template = kwargs.get('template', None)
    if not template:
        raise Http404

    template = '.'.join([template, 'html'])
    title = kwargs.get('title', 'static page')
    img = kwargs.get('img', 'bgag.jpg')
    return render_to_response(template, {
        'page_title': title,
        'menu': get_menu(),
        'page_img': img,
        })


def get_page_title(lb):
    """Fills page title."""
    if lb:
        return "%s: %s" % (settings.PROJECT_NAME, lb)
    return settings.PROJECT_NAME
