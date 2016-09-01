from django.conf.urls import url

from . import views


urlpatterns = (
    url(r'^$', views.build_index, {
        'label': 'index',
        'template': 'collectionv',
        'img': 'bg_main1.jpg'
        }),
)
