# -*- coding:utf-8 -*-
"""
parse web content about league,now it includes:premier league,Liga BBVA
"""

import re
from collections import defaultdict

import requests
from bs4 import BeautifulSoup
from prettytable import PrettyTable

from FBRank.utils.exceptions import IllegalArgumentException
from FBRank.utils.utils import league_news_pattern

league_news_pattern_target = re.compile(league_news_pattern)


def parse_league_rank(url, index=0):
    """
    :param url: weburl which contains ceatain league rank information
    :return: PrettyTable Object contains league rank

    tips:
    - origin premire leagure website will be instability
    - sports tencent return JSON Data,But cannot be directy play(with out front-end)
    url = "http://matchweb.sports.qq.com/team/rank"
    payloads = 
         'callback': 'recommendlist',
         'competitionId': '8',
         'from': 'sporthp',
         '_': str(randint(1, 100000))
     }
    response = requests.get(url, params=payloads).content.decode('utf-8')
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
    :return: dict {index:[title,url]}
    """
    news_dict = defaultdict(list)
    web_news = requests.get(url).content.decode('utf-8')
    key = 1
    for url, title in league_news_pattern_target.findall(web_news):
        news_dict[key].extend([url, title])
        key += 1
    return news_dict


def show_news(news_dict):
    table = PrettyTable(["ID", "链接"])
    for id, (_, title) in news_dict.items():
        table.add_row([id, title])
    print(table)
    prompt = input('------请输入选择的 id 查看新闻具体内容，或者点击 q 退出------\n')
    if prompt == 'q':
        return '点击结束'
    else:
        pass


def get_news_from_index(url):
    """
    get wen news from certain url
    :param url: new url
    :return: new content,plain text
    """
