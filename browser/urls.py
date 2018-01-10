from django.conf.urls import url

from . import views


urlpatterns = (
    url(r'^$', views.view_content, {'template': 'multicol'}),
    url(r'^watch/$', views.view_content, {'template': 'multicol'}),
    url(r'^listen/$', views.view_content, {'template': 'multicol'}),
    url(r'^read/$', views.view_content, {'template': 'multicol'}),
    url(r'^rider/$', views.view_content, {'template': 'multicol'}),
    url(r'^contact/$', views.view_content, {'template': 'multicol'}),
    url(r'^reviews/$', views.view_content, {'template': 'multicol'}),
    url(r'^press/$', views.view_content, {'template': 'multicol'}),
    url(r'^404/$', views.view_static, {'template': '404'}),
)
