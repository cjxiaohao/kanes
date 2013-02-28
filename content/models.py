from django.db import models
from django.db.models.signals import pre_save
from util import Revision
from pdb import set_trace as bp

class Content ( models.Model ):
    slug = models.SlugField ( )
    body = models.TextField ( )
    revisions = models.IntegerField ( editable = False, default = 0 )

    def __init__ ( self, *args, **kwargs ):
        super ( Content, self ).__init__ ( *args, **kwargs )
        self.previous_body = self.body

    def make_revision ( self ):
        self.revisions += 1
        revision = Revision ( self.previous_body, self.body )
        c = Changelog ( content = self, body = revision.diff, additions = \
                    revision.additions, deletions = revision.deletions )
        c.save ( )

class Changelog ( models.Model ):
    content = models.ForeignKey ( Content )
    body = models.TextField ( )
    additions = models.IntegerField ( )
    deletions = models.IntegerField ( )

def pre_save_content ( sender, **kwargs ):
    instance = kwargs['instance']

    if instance.pk:
        instance.make_revision ( )

pre_save.connect ( pre_save_content, sender = Content )
