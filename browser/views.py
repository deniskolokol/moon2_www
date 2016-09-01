#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
import random

from django.http import Http404, HttpResponse
from django.shortcuts import render_to_response
from django.conf import settings


comp_name = 'moon2'


def build_index(request, **kwargs):
    """
    Build Index page
    """
    # WARNING! Change to processing of the index when its ready
    page_label = kwargs.get('label', '')
    page_template = kwargs.get('template', '')
    page_img = kwargs.get('img', 'bg_main1.jpg')
    if not page_template:
        raise Http404

    page_template = '.'.join([page_template, 'html'])
    data_dict = get_data_index()
    data = ((
        data_dict['main'], data_dict['video'], data_dict['audio'],
        ), )
    return render_to_response(page_template, {
        'page_title': get_page_title(page_label.strip()),
        'data': data,
        'menu': get_menu(),
        'page_img': page_img,
        'static_url': settings.STATIC_URL
        })


def get_page_title(lb):
    """
    Fill page title
    """
    page_ttl = comp_name
    if lb:
        page_ttl += ': ' +  lb

    return page_ttl


def get_menu():
    return [
        {'label': 'index', 'uri': ''},
        {'label': 'listen', 'uri': 'http://sympliromatiko.net/audio/'},
        {'label': 'watch', 'uri': 'http://sympliromatiko.net/video/'},
        {'label': 'read', 'uri': 'http://sympliromatiko.net/about/'},
        {'label': 'rider', 'uri': 'http://sympliromatiko.net/tech-rider/'},
        {'label': 'contact', 'uri': 'http://sympliromatiko.net/contacts/'},
        ]


############################################################
# extracting data
# WARNING! to be extracted from db!!

def get_data_index():
    return {
    'main': {
        'title': 'MOON2',
        'text': """<i>inhuman music made by humans for a humankind</i>
        <p>
        Imagine if you could touch the sounds surrounding you. Imagine if you could build a piece of music by simply grabbing and moving sounds around, as if they were sticks and stones. Imagine yourself becoming a Titan in a vast sonic Universe moving and smashing massive masses of sounds around you.
        <p>
        MOON2 (formely Sympli Romatikó) is a trio with more or less stable residence in Kraków, Poland. The group’s main focus is interactive performance, algorithmic composition, virtual worlds, this kind of stuff… Pretty scientific and inhuman, but made by humans and for a humankind.
        """
        },
    'video': {
        'title': '',
        'text': """<iframe src="https://player.vimeo.com/video/134827501?title=0&byline=0&portrait=0" width="300" height="169" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen></iframe>"""
        },
    'audio': {
        'title': '',
        'text': """<iframe style="border: 0; width: 300px; height: 300px;" src="https://bandcamp.com/EmbeddedPlayer/album=858428838/size=large/bgcol=333333/linkcol=0f91ff/minimal=true/transparent=true/" seamless><a href="http://mathka.bandcamp.com/album/sympli-romatik">Sympli Romatikó by Sympli Romatikó</a></iframe>"""
    }
}
