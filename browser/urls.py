from django.conf.urls import url

from . import views


urlpatterns = (
    url(r'^$', views.view_content, {'template': 'multicol', 'section': 'index'}),
    url(r'^watch/$', views.view_content, {'template': 'multicol', 'section': 'watch'}),
    url(r'^listen/$', views.view_content, {'template': 'multicol', 'section': 'listen'}),
    url(r'^read/$', views.view_content, {'template': 'multicol', 'section': 'read'}),
    url(r'^rider/$', views.view_content, {'template': 'multicol', 'section': 'rider'}),
    url(r'^contact/$', views.view_content, {'template': 'multicol', 'section': 'contact'}),
    url(r'^reviews/$', views.view_content, {'template': 'multicol', 'section': 'reviews'}),
    url(r'^404/$', views.view_static, {'template': '404'}),
)
