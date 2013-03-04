from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'_/write/(?P<path>[\w\/]+)?$', 'content.views.write', name='content_write'),
    url(r'(?P<user>\w+)\/(?P<path>[\w+\/]+)?$', 'content.views.view', \
        name='content_view'),
)
