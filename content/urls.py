from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'write$', 'content.views.write', name='write'),
)
