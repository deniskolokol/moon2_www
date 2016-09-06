from django.conf.urls import url

from . import views


urlpatterns = (
    url(r'^$', views.view_index, {
        'label': 'index',
        'template': 'column_left',
        'img': 'bg1.jpg'
        }),
    url(r'^watch/$', views.view_watch, {
        'label': 'watch',
        'template': 'row_top',
        'img': 'bg5.jpg'
        }),
    url(r'^read/$', views.view_read, {
        'label': 'about',
        'template': 'row_bottom',
        'img': 'bg4.jpg'
        }),
)
