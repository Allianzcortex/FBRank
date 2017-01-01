# -*- coding:utf-8 -*-

import re

import requests
from bs4 import BeautifulSoup
from prettytable import PrettyTable

from FBRank.utils.exceptions import IllegalArgumentException


def parse_league_rank(url, index=0):
    """
    :param url: weburl which contains ceatain league rank information
    :return: PrettyTable Object contains league rank

    tips:
    - origin premire leagure website will be instability
    - sprts tencent return JSON Data,But cannot be directy play(with out front-end)
    url = "http://matchweb.sports.qq.com/team/rank"
    payloads = 
         'callback': 'recommendlist',
         'competitionId': '8',
         'from': 'sporthp',
         '_': str(randint(1, 100000))
     }
    response = requests.get(url, params=payloads).content.decode('utf-8')
    print (response)
    """

    cur = 1
    table = PrettyTable(["排名", "球队名", "场次", "胜", "平", "负", "进球", "失球",
                         "净胜球", "场均进球", "场均失球", "场均净胜", "场均积分", "积分"])
    soup = BeautifulSoup(requests.get(url).content.decode("utf-8"), "lxml")
    for t in soup.find_all("tr", class_=re.compile(r"trbg[red|yellow|blue|grey]")):
        club = [c.get_text() for c in t.find_all("td") if c.get_text()]
        if (cur == index):
            return club
        cur += 1
        table.add_row(club)
    if index != 0:
        raise IllegalArgumentException(
                "index out of range,the max is {} /排名超出范围，最大是 {}".format(cur, cur))
    return table

def parse_league_news(url):
    """
    :param url: weburl which contains ceatain league news information
    :return: 
    """