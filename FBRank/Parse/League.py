# -*- coding:utf-8 -*-

import re

import requests
from bs4 import BeautifulSoup
from prettytable import PrettyTable


def parse_league_rank(url):
    table = PrettyTable(["排名", "球队名", "场次", "胜", "平", "负", "进球", "失球",
                         "净胜球", "场均进球", "场均失球", "场均净胜", "场均积分", "积分"])
    soup = BeautifulSoup(requests.get(url).content.decode("utf-8"), "lxml")
    for t in soup.find_all("tr", class_=re.compile(r"trbg[red|yellow|blue|grey]")):
        club = [c.get_text() for c in t.find_all("td") if c.get_text()]
        table.add_row(club)

    return table
