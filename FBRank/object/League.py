# -*- coding:utf-8

from FBRank.parse.League import parse_league_rank, parse_league_news, show_news
from FBRank.utils.utils import league_configure, league_transformat
from FBRank.utils.exceptions import IllegalNameException


class League(object):
    def __init__(self, pass_name):
        self.name = self._get_name(pass_name)  # to be converted
        self.rank = self._get_webrank()
        self.news = self._get_news()

    def _get_name(self, pass_name):
        for league_list in league_transformat.keys():
            if pass_name in league_list or pass_name.lower() in league_list:
                return league_transformat.get(league_list)

        raise IllegalNameException("")

    def _get_news(self):
        news_dict = parse_league_news(self._get_news_url())
        show_news(news_dict)

    def _get_news_url(self):
        return league_configure[self.name]['news_url']

    def _get_webrank(self, index=0):
        return parse_league_rank(self._get_webrank_url(), index)

    def _get_webrank_url(self):
        return league_configure[self.name]['rank_url']
