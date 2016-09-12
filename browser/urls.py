from django.conf.urls import url

from . import views


urlpatterns = (
    url(r'^$', views.view_content, {'template': 'column_left', 'section': 'index'}),
    url(r'^watch/$', views.view_content, {'template': 'row_top', 'section': 'watch'}),
    url(r'^listen/$', views.view_content, {'template': 'row_top', 'section': 'listen'}),
    url(r'^read/$', views.view_content, {'template': 'row_bottom', 'section': 'read'}),
    url(r'^rider/$', views.view_content, {'template': 'column_left', 'section': 'rider'}),
    url(r'^contact/$', views.view_content, {'template': 'row_top', 'section': 'contact'}),
)
