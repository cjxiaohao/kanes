from django.contrib import admin
from .models import Content, Changelog

class ContentAdmin ( admin.ModelAdmin ):
    pass

class ChangelogAdmin ( admin.ModelAdmin ):
    pass

admin.site.register ( Content, ContentAdmin )
admin.site.register ( Changelog, ChangelogAdmin )
