#!-*- encoding:utf-8 -*-

import difflib
import unittest
from content.util import Revision


# 还没有考虑上下文的情况
class RevisionTestCase ( unittest.TestCase ):

    def test_diff ( self ):
        a = [ "1", "1", "2", "4"]
        b = [ "1", "1", "3", "2"]

        a2 = [ "1", "1", "1", "!" ]

        a = a2 + a
        b = a2 + b

        r = Revision ( "\n".join ( a ), "\n".join ( b ) )
        self.assertEqual ( 1, r.additions )
        self.assertEqual ( 1, r.deletions )

