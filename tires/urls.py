from django.conf.urls import url

from . import views

app_name = 'tires'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<pk>[0-9]+)/$', views.TireView.as_view(), name='detail'),
]
