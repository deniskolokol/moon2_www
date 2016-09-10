from django.conf.urls import url

from . import views


urlpatterns = (
    url(r'^$', views.view_index, {
        # XXX - move this all to db
        'label': 'index',
        'template': 'column_left',
        'img': 'bg1.jpg'
        # XXX
        }),
    url(r'^watch/$', views.view_watch, {
        'label': 'watch',
        'template': 'row_top',
        'img': 'bg5.jpg'
        }),
    url(r'^listen/$', views.view_listen, {
        'label': 'listen',
        'template': 'row_top',
        'img': 'bg6.jpg'
        }),
    url(r'^read/$', views.view_read, {
        'label': 'about',
        'template': 'row_bottom',
        'img': 'bg4.jpg'
        }),
    url(r'^rider/$', views.view_rider, {
        'label': 'tech-rider',
        'template': 'column_left',
        'img': 'bg2.jpg'
        }),
    url(r'^contact/$', views.view_contact, {
        'label': 'contact',
        'template': 'row_top',
        'img': 'bg3.jpg'
        }),
)
