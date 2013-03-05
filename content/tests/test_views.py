import unittest
from django.test.client import Client
from pdb import set_trace as bp
from content.models import Content

class ContentViewTestCase ( unittest.TestCase ):
    USER = "test"
    PASS = "test"

    def setUp ( self ):
        self.client = Client ( )
        self.client.login ( username = self.USER, password = self.PASS )

    def test_write ( self ):
        response = self.client.post ( "/_/write/", {\
            "slug": "test2",
            "body": "2"
        }, follow = True )

        content = Content.objects.get ( slug = "test2" )

        self.assertEquals ( self.USER, content.user.username )
        self.assertEquals ( 'test2', response.context['content'].slug )

    def test_write_exists ( self ):
        response = self.client.post ( "/_/write/?slug=test2", {\
            "body": "3" } )
        self.assertEquals ( 200, response.status_code )

    def test_path_has_space ( self ):
        response = self.client.get ( "/%s123/test%%201" % self.USER )
        self.assertEquals ( 200, response.status_code )

    def test_view ( self ):
        response = self.client.get ( "/%s/test1" % self.USER )
        self.assertEquals ( 200, response.status_code )