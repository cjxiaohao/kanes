#!-*- encoding:utf-8 -*-

import unittest
from content.models import Content, Changelog
from pdb import set_trace as bp 

class ContentTestCase ( unittest.TestCase ):

    REVISION_DIFF = """@@ -1 +1,2 @@\n one\n+two"""

    def test_fully_content_save ( self ):
        """ 测试signal是否正确执行
        """
        c1 = Content ( slug = "test_signal", body = "one" )
        c1.save ( )

        c2 = Content.objects.get ( slug = "test_signal" )
        c2.body = "one\ntwo"
        c2.save ( )


        self.assertEqual ( 1, Content.objects.get ( slug = "test_signal" )\
            .revisions )

        revision1 = c2.changelog_set.all ()[0]

        self.assertEqual ( 1, revision1.additions )
        self.assertEqual ( 0, revision1.deletions )
        self.assertEqual ( 1, revision1.revision )

        self.assertEqual ( self.REVISION_DIFF, revision1.body )
