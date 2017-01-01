# -*- coding:utf-8 -*-

"""
Entry Point Enterration
"""
from __future__ import print_function
import argparse
import sys
from os import path
sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))

from FBRank.object.League import League


# from FBRank.utils.utils import PY2

def execute():
    parser = argparse.ArgumentParser(description="load football list")
    parser.add_argument("-l", "--league", dest="league")
    parser.add_argument("ask", default="rank", choices=["rank", "info", "news"])
    args = parser.parse_args()

    # deal with league
    league_name = vars(args).get('league')
    league = League(league_name)
    print(league.rank)


if __name__ == '__main__':
    execute()
