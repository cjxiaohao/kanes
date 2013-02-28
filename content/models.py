from django.db import models

class Content ( models.Model ):
    slug = models.SlugField ( )
    body = models.TextField ( )
    revisions = models.IntegerField ( editable = False, default = 0 )

class Changelog ( models.Model ):
    content = models.ForeignKey ( Content )
    body = models.TextField ( )
    additions = models.IntegerField ( )
    deletions = models.IntegerField ( )
