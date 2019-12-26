# -*- coding:utf-8 -*-

import unittest
import sys

sys.path.append('../FBRank')
from FBRank.object import League
from FBRank.parse.League import get_news_from_index
from FBRank.utils.exceptions import IllegalNameException


# def test_error():
#     raise ValueError("dd")

class TestLeague(unittest.TestCase):
    def setUp(self):
        self.league = League("EPL")

    def test_construct(self):
        # self.assertRaises(ValueError,test_error)
        self.assertRaises(IllegalNameException, League, "cc")

    def test_attribute(self):
        self.assertTrue(hasattr(self.league, 'rank'))

    def test_news(self):
        self.assertTrue(get_news_from_index(
                "http://slide.sports.sina.com.cn/g_pl/slide_2_61364_119344.html/d/1#p=1") is not None)


if __name__ == '__main__':
    unittest.main()
