from django.db import models
from django.db.models.signals import pre_save
from django.contrib.auth.models import User
from util import Revision
from datetime import datetime
from pdb import set_trace as bp

class Content ( models.Model ):
    user = models.ForeignKey ( User, editable = False, default = 0 )
    slug = models.CharField ( max_length = 255, db_index = True, unique = True )
    body = models.TextField ( )
    revisions = models.IntegerField ( editable = False, default = 0 )
    update_at = models.DateTimeField ( auto_now = True, auto_now_add = True, \
                                       editable = False, default = \
                                       datetime.now ( ) )
    create_at = models.DateTimeField ( auto_now_add = True, editable = False, \
                                       default = datetime.now ( )  )

    def __init__ ( self, *args, **kwargs ):
        super ( Content, self ).__init__ ( *args, **kwargs )
        self.previous_body = self.body

    def __unicode__ ( self ):
        return self.slug

    def make_revision ( self ):
        self.revisions += 1
        revision = Revision ( self.previous_body, self.body )
        c = Changelog ( content = self, body = revision.diff, additions = \
                        revision.additions, deletions = revision.deletions, \
                        revision = self.revisions )
        c.save ( )

class Changelog ( models.Model ):
    revision = models.IntegerField ( default = 0 )
    content = models.ForeignKey ( Content )
    body = models.TextField ( )
    additions = models.IntegerField ( )
    deletions = models.IntegerField ( )

    create_at = models.DateTimeField ( auto_now_add = True, editable = False, \
                                       default = datetime.now ( ) )

    def __unicode__ ( self ):
        return "user: %s, %s revision:%d" % ( self.content.user.username, \
                                    self.content.slug, self.revision )

def pre_save_content ( sender, **kwargs ):
    instance = kwargs['instance']

    if instance.pk:
        instance.make_revision ( )

pre_save.connect ( pre_save_content, sender = Content )
