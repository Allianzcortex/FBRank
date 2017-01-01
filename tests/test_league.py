# -*- coding:utf-8 -*-

import unittest
import sys

sys.path.append('../FBRank')

from FBRank.object import League
from FBRank.utils.exceptions import IllegalNameException


# def cc():
#     raise ValueError("dd")

class TestLeague(unittest.TestCase):
    def setUp(self):
        self.league = League("英超")

    def test_construct(self):
        # self.assertRaises(ValueError,cc)
        self.assertRaises(IllegalNameException, League, "cc")

    def test_attribute(self):
        self.assertTrue(hasattr(self.league, 'rank'))


if __name__ == '__main__':
    unittest.main()
