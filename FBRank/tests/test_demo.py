# -*- coding:utf-8 -*-

# import argparse
#
# parser = argparse.ArgumentParser(description='Process some integers.')
# parser.add_argument('integers', metavar='N', type=int, nargs='+',
#                     help='an integer for the accumulator')
# parser.add_argument('--sum', dest='accumulate', action='store_const',
#                     const=sum, default=max,
#                     help='sum the integers (default: find the max)')
#
# args = parser.parse_args()
# print(args.accumulate(args.integers))
import re
from random import randint

import requests
from bs4 import BeautifulSoup


from prettytable import PrettyTable


def test():
    # 英超官网被墙了,SS 可以访问但 requests 不可以

    # 腾讯体育返回的是 JSON 数据，但不包含具体的球队排名信息，还会由前端进行处理
    # url = "http://matchweb.sports.qq.com/team/rank"
    # payloads = {
    #     'callback': 'recommendlist',
    #     'competitionId': '8',
    #     'from': 'sporthp',
    #     '_': str(randint(1, 100000))
    # }
    # response = requests.get(url, params=payloads).content.decode('utf-8')
    # print (response)

    # 新浪体育包含的参数更多。。。

    # 考虑虎扑

    table = PrettyTable(["排名", "球队名", "场次", "胜", "平", "负", "进球", "失球",
                         "净胜球", "场均进球", "场均失球", "场均净胜", "场均积分", "积分"])
    url = "http://soccer.hupu.com/table/England.html"
    soup = BeautifulSoup(requests.get(url).content.decode("utf-8"), "lxml")
    for t in soup.find_all("tr", class_=re.compile(r"trbg[red|yellow|blue|grey]")):
        club = [c.get_text() for c in t.find_all("td") if c.get_text()]
        table.add_row(club)

    print(table)
    # 接下来考虑 prettytable
    table = PrettyTable(["name", "city"])
    table.add_row(["tom", "New York"])
    print(table)


if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser(description="load football list")
    parser.add_argument("-l", "--league", dest="league")
    parser.add_argument("ask", default="rank", choices=["rank", "info", "news"])
    args = parser.parse_args()
    print(vars(args))

    test()
