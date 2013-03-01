from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'(?P<user>\w+)\/(?P<path>[\w+\/]+)?$', 'content.views.view', \
        name='view'),
    url(r'_/write/([\w\/]+)?$', 'content.views.write', name='write'),
)
