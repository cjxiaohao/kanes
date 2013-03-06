from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^_/$', 'content.views.all', name='content_all' ),
    url(r'_/write/(?P<path>[\w\d\s\.\/]+)?$', 'content.views.write', name='content_write'),
    url(r'_/revsion/(?P<user>[\w\d]+)\/(?P<path>[\w\d\s\.\/]+)?', 'content.views.revision', name='content_revision' ),
    url(r'^(?P<user>[\w\d]+)\/(?P<path>[\w\d\s\.\/]+)?$', 'content.views.view', \
        name='content_view'),
)
