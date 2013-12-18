from django.conf.urls import patterns, url
from testapps import views

urlpatterns = patterns('testapps',
    url(r'^$', 'views.index', name='index'),
    url(r'^/(?P<testapp_id>\d+)$', 'views.show', name='show'),
    url(r'^/(?P<testapp_id>\d+)/urlendsinslash/$', 'views.slashed', name='slashed'),
)