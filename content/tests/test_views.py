import unittest
from django.test.client import Client

class ContentViewTestCase ( unittest.TestCase ):
    def setUp ( self ):
        self.client = Client ( )
        self.client.login ( username = 'test', password = 'test' )

    def test_write ( self ):
        self.client.post ( "/content/write", {\
            "slug": "test2",
            "body": "2"
        } )

    def test_write_exists ( self ):
        self.client.post ( "/content/write?slug=test2", {\
            "body": "3" } )
