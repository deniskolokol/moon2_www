#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
import random

from django.http import Http404, HttpResponse
from django.shortcuts import render_to_response
from django.conf import settings

from core.models import Content
from .models import SocialResource, MenuItem


def get_section(request):
    try:
        return MenuItem.objects.get(uri=request.path).label
    except MenuItem.DoesNotExist:
        return [x.strip() for x in request.path.rsplit('/') if x != ''][0]


def view_content(request, **kwargs):
    """Outputs specified page."""
    template = kwargs.get('template', None)
    if not template:
        template = "multicol"
    if not template.endswith('.html'):
        template += '.html'
    section = get_section(request)
    data = Content.get_columns(section__label=section, section__is_active=True)
    page_img = data[0][0].section.bg_image + ".jpg"
    if not page_img.endswith('.jpg'):
        page_img += '.jpg'
    return render_to_response(
        template,
        {
            'is_mobile': request.user_agent.is_mobile,
            'page_title': get_page_title(section),
            'content': data,
            'menu': MenuItem.active().order_by('order_id'),
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
        'is_mobile': request.user_agent.is_mobile,
        'page_title': title,
        'menu': MenuItem.active().order_by('order_id'),
        'page_img': img,
        })


def get_page_title(lb):
    """Fills page title."""
    if lb:
        return "%s: %s" % (settings.PROJECT_NAME, lb)
    return settings.PROJECT_NAME
