#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
import random

from django.http import Http404, HttpResponse
from django.shortcuts import render_to_response
from django.conf import settings


def get_struct(request, content, **kwargs):
    page_label = kwargs.get('label', '')
    page_template = kwargs.get('template', '')
    page_img = kwargs.get('img', 'bg1.jpg')
    if not page_template:
        raise Http404
    page_template = '.'.join([page_template, 'html'])
    return render_to_response(page_template, {
        'page_title': get_page_title(page_label.strip()),
        'content': content,
        'menu': get_menu(),
        'page_img': page_img,
        'static_url': settings.STATIC_URL
        })


def view_index(request, **kwargs):
    """Builds Index page."""
    cont = get_index()
    content = (
        (cont['main'], cont['video'], cont['audio'],),
        )
    return get_struct(request, content, **kwargs)


def view_watch(request, **kwargs):
    """Builds 'watch' page (video)."""
    cont = get_watch()
    content = (
        (cont['main'], ),
        (cont['aux'], ),
        (cont['media'],),
        )
    return get_struct(request, content, **kwargs)


def view_read(request, **kwargs):
    """Builds 'read' page (about)."""
    cont = get_about()
    content = (
        (cont['main'], ),
        (cont['media'],),
        (cont['aux'], ),
        )
    return get_struct(request, content, **kwargs)


def get_page_title(lb):
    """Fills page title."""
    if lb:
        return "%s: %s" % (settings.PROJECT_NAME, lb)
    return settings.PROJECT_NAME


def get_menu():
    return [
        {'label': 'index', 'uri': '/'},
        {'label': 'watch', 'uri': '/watch/'},
        {'label': 'read', 'uri': '/read/'},
        {'label': 'listen', 'uri': 'http://sympliromatiko.net/audio/'},
        {'label': 'rider', 'uri': 'http://sympliromatiko.net/tech-rider/'},
        {'label': 'contact', 'uri': 'http://sympliromatiko.net/contacts/'},
        ]


############################################################
# extracting data
# WARNING! to be extracted from db!!

def get_index():
    return {
    "main": {
        "title": "MOON2",
        "text": """<i>inhuman music made by humans for a humankind</i>
        <p>
        Imagine if you could touch the sounds surrounding you. Imagine if you could build a piece of music by simply grabbing and moving sounds around, as if they were sticks and stones. Imagine yourself becoming a Titan in a vast sonic Universe moving and smashing massive masses of sounds around you.
        <p>
        MOON2 (formely Sympli Romatikó) is a trio with more or less stable residence in Kraków, Poland. The group’s main focus is interactive performance, algorithmic composition, virtual worlds, this kind of stuff… Pretty scientific and inhuman, but made by humans and for a humankind.
        """
        },
    "video": {
        "title": "",
        "text": """<iframe src="https://player.vimeo.com/video/134827501?title=0&byline=0&portrait=0" width="300" height="169" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen></iframe>"""
        },
    "audio": {
        "title": "",
        "text": """<iframe style="border: 0; width: 300px; height: 300px;" src="https://bandcamp.com/EmbeddedPlayer/album=858428838/size=large/bgcol=333333/linkcol=0f91ff/minimal=true/transparent=true/" seamless><a href="http://mathka.bandcamp.com/album/sympli-romatik">Sympli Romatikó by Sympli Romatikó</a></iframe>"""
    }
}


def get_watch():
    return {
    "main": {
        "title": "MOON2",
        "text": """<i>is a virtual world with simplified physical laws,</i>
        <br>
        where sounds turn into objects, whose behavior is affected by natural forces such as gravity and wind. Performer’s hands attract floating sounds – he literally “grasps” them and “draws” their trajectories in space. The space itself is a giant ephemeral musical instrument, which you neither pluck, nor bow, but excite through movement."""
        },
    "aux": {
        "title": "",
        "text": """It is neither about dance, nor interactive electronic music, nor whatever fancy label one can come up with. It is about a human body simultaneously operating in so-call reality as well as in the virtual World, which we can only hear.
        <p>
        Interested in having us around? Please, take a look at our tech-rider (<a href="https://drive.google.com/file/d/0B0RqX5ckmV-mTm4ySHRvOGJrVlU/">stereo</a> | <a href="https://drive.google.com/file/d/0B0RqX5ckmV-mbDhyRER0b2NPRW8/">surround</a>) and <a href="/contact/">contact us</a>.
        <p><a href="http://sympliromatiko.net/video/">More videos</a>
        """
        # XXX instead of "More videos" add small pictograms with links to youtube & vimeo
        },
    "media": {
        "title": "",
        "text": """<iframe src="https://player.vimeo.com/video/134404722?title=0&byline=0&portrait=0" width="300" height="169" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen></iframe>"""
    }
}

def get_about():
    return {
    "main": {
        "title": "MOON2",
        "text": """<i>Denis Kolokol, electronics, movement;
        <br>Ernest Ogórek, bass;
        <br>Tomek Chołoniewski, drums.</i>
        <p>
        MOON2 is a trio with more or less stable residence in Kraków, Poland. The group’s main focus is interactive performance, algorithmic composition, virtual worlds, this kind of stuff... Pretty scientific and inhuman, but made by humans and for a humankind.
        """
        # XXX add small pictograms with links to full-size pictures
        },
    "aux": {
        "title": "",
        "text": """We see music not as a sequence of events, but as a dynamic system, which we only pretend to control. If an order becomes slightly more complicated, than the simple “if-else” directive, the system tends to fall apart as more and more hidden inconsistencies unfold. These anomalies is our material. We balance on the surface of the meticulously painted chart trying not to be buried under the pure chaos.
        <p>
        All the electronic sounds are programmed manually in <a href="http://supercollider.github.io/">SuperCollider</a>. No commercial synths used.
        """
        },
    "media": {
        "title": "",
        "text": """<a href="/static/img/portrait.jpg"><img src="/static/img/portrait_s.jpg" border="0" /></a>"""
    }
}
