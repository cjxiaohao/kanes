import unittest
from django.http import Http404
from django.template import TemplateDoesNotExist
from django.test.client import Client
from pdb import set_trace as bp
from content.models import Content
from django.contrib.auth.models import User
from BeautifulSoup import BeautifulSoup

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
        response = self.client.post ( "/_/write/test2", {\
            "body": "3" } )
        self.assertEquals ( 302, response.status_code )

    def test_write_not_has_permission ( self ):
        # with self.assertRaises ( TemplateDoesNotExist ) as error:
        response = self.client.post ( "/_/write/test 1", {\
            "body": "3" } )

        self.assertEquals ( 302, response.status_code )

        user = User.objects.get ( username = self.USER )
        self.assertNotEqual ( None,
                              Content.objects.get ( user = user,
                                                    slug = "test 1" ) )
    def test_write_not_has_path ( self ):
        response = self.client.get ( "/test/" )


    def test_path_has_space ( self ):
        response = self.client.get ( "/%s123/test%%201" % self.USER )
        self.assertEquals ( 200, response.status_code )

    def test_view ( self ):
        response = self.client.get ( "/%s/test1" % self.USER )
        self.assertEquals ( 200, response.status_code )

    def test_view_is_private ( self ):
        response = self.client.get ( "/%s123/test3" % self.USER )

        self.assertEquals ( 404, response.status_code )

    def test_view_not_has_action ( self ):
        response = self.client.get ( "/%s123/test 1" % self.USER )
        soup = BeautifulSoup ( response.content )
        self.assertEquals ( None, soup.find ( "li", { "id": "action" } ) )

    def test_content_not_exists ( self ):
        response = self.client.get ( "/%s/notexists" % self.USER )
        soup = BeautifulSoup ( response.content )
        path = soup.find ( "input", { "name": "slug" } )
        self.assertEquals ( "notexists", dict(path.attrs)['value'] )
        