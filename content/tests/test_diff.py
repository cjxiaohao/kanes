#!-*- encoding:utf-8 -*-

import difflib
import unittest


# 还没有考虑上下文的情况
class DiffTestCase ( unittest.TestCase ):

    def test_diff ( self ):
        a = [ "1", "1", "2", "4"]
        b = [ "1", "1", "3", "2"]

        a2 = [ "1", "1", "1", "!" ]

        a = a2 + a
        b = a2 + b

        diffs = difflib.unified_diff ( a, b )
        i = 1
        additions = 0
        deletions = 0
        regroup = []
        for d in diffs:
            print [d]
            if i > 2:
                if i == 3:
                    d = d[:-1]
                regroup.append ( d )
            if i > 3:
                if d[0] == "+":
                    additions += 1
                elif d[0] == "-":
                    deletions += 1
            i += 1

        print "Addition lines: %d deletion lines: %d" % ( additions, deletions
        )

        print "\n".join ( regroup )

