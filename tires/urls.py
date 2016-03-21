from django.conf.urls import url

from . import views

app_name = 'tires'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^catalog/(?P<slug>[\w-]+)/$', views.DetailView.as_view(), name='detail'),
    url(r'list/$', views.TiresListView.as_view(), name='tiresList'),
    url(r'^api/get_tires/', views.get_tires, name='get_tires'),

]
