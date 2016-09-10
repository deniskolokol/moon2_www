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


def view_listen(request, **kwargs):
    """Builds 'listen' page (music)."""
    cont = get_listen()
    content = (
        (cont['main'], ),
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


def view_contact(request, **kwargs):
    """Builds 'contact' page."""
    cont = get_contact()
    content = (
        (cont['main'], ),
        (cont['media'],),
        )
    return get_struct(request, content, **kwargs)


def view_rider(request, **kwargs):
    """Builds 'contact' page."""
    cont = get_rider()
    content = (
        (cont['main'], cont['aux'], cont['media'],),
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
        {'label': 'listen', 'uri': '/listen/'},
        {'label': 'read', 'uri': '/read/'},
        {'label': 'rider', 'uri': '/rider/'},
        {'label': 'contact', 'uri': '/contact/'},
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


def get_listen():
    return {
        "main": {
            "title": "",
            "text": """<iframe width="430" height="120" scrolling="no" frameborder="no" src="https://w.soundcloud.com/player/?url=https%3A//api.soundcloud.com/playlists/16549058&amp;color=e54b29&amp;auto_play=false&amp;show_user=true&amp;show_reposts=false"></iframe>"""
            },
        "media": {
            "title": "",
            "text": """<iframe style="border: 1; border-width: 6px; border-style: solid; border-radius: 5px; border-color: #f5f5f5; width: 430px; height: 110px;" src="https://bandcamp.com/EmbeddedPlayer/album=858428838/size=large/bgcol=ffffff/linkcol=de270f/tracklist=false/artwork=small/transparent=true/" seamless><a href="http://mathka.bandcamp.com/album/sympli-romatik">Sympli Romatikó by Sympli Romatikó</a></iframe>"""
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


def get_contact():
    return {
        "main": {
            "title": "MOON2 contacts",
            "text": """speak to <i>Denis Kolokol</i> +48 508 986 079
            <br/>or write to <i>moon2.band AT gmail DOT com</i>"""
            },
        "media": {
            "title": "",
            "text": """"""
            }
        }


def get_rider():
    return {
        "main": {
            "title": "",
            "text": """<h5>Electronics</h5>
            2 speakers powerful enough for the room.
            <br/>Cables to connect audio interface with the main mixer (mono-outputs 1/4'' TRS). Subwoofer(s) powerful enough for the room (summary from all channels, except bass).
            <h5>Bass</h5>
            Bass amplifier on stage powerful enough for the room.
            <h5>Drums</h5>
            A drum kit: bass drum with pedal, snare drum with stand, floor tom, two hanging toms, hi-hat stand, 3 cymbal stands, drum chair, additional normal chair, carpet (if needed). Warning! The drum kit isn't needed for gigs taking place in Kraków. Instead the transportation of the drum kit to and fro is required.
            <br/>Mic set for amplification of the drum kit.
            <h5>Monitoring</h5>
            2 mono stage monitors, with summary from all channels on the main mixer. Warning! Monitors should be placed as close to the speakers as possible (see image).
            <h5>Other</h5>
            Table for electronics (approx 120x70cm, any height).
            <br/>Stand for Kinect (not higher than 70cm above the surface, on which a frontman stands). AC: 5 sockets for electronics according to your country standards.
            <h5>Lights</h5>
            Dim light with the dominance of red color. Static red spots on each band member.
            <h5>Optional</h5>
            Stage platform or scene approx 30-50cm high.
            <br/><b>Warning!</b> For gigs taking place in Kraków: transportation of the drum kit (to and fro).
            <h5>Calibration and check</h5>
            2.5 hrs soundcheck. Warning! Critical for properly calibrating the space and amplifying the
drums!
            <br/>Light and sound engineers available during the calibration and sound / light-check."""
            },
        "aux": {
            "title": "stereo",
            "text": """<a href="https://drive.google.com/file/d/0B0RqX5ckmV-mNDNtbmZidElmVk0/"><img src="/static/img/moon2rider_stereo.jpg" border="0" /></a>"""
            },
        "media": {
            "title": "surround",
            "text": """<a href="https://drive.google.com/file/d/0B0RqX5ckmV-mWlZTdGp2Z2QteFE/"><img src="/static/img/moon2rider_surround.jpg" border="0" /></a>"""
            }
        }
