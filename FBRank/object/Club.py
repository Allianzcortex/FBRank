# -*- coding:utf-8 -*-
"""
Use For All Club
One CLub should hava attributes as folowing:
- name
- create_time
- Court
- coach
- belog_league

The Logic and Content will be very simple,so there is no need to write parse/Club.py
"""

from FBRank.utils.utils import league_transformat, check_before
from FBRank.utils.exceptions import IllegalNameException

import requests
from bs4 import BeautifulSoup


class Club(object):
    def __init__(self, intro_name):
        self.name = intro_name
        # if use soup as property,then when try to get attribute,every hit will ask for one web url
        if self.name.lower() in league_transformat.keys():
            self.web_url = ''
            self.soup = BeautifulSoup(requests.get(self.web_url).text)

    @property
    @check_before()
    def create_time(self):
        return self.soup.find_all().text

    @property
    @check_before()
    def court(self):
        """
        TODO implement
        :return:
        """

    def __repr__(self):
        return '<Club {}>'.format(self.name)
