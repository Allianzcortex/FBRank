# -*- coding:utf-8 -*-
import sys
from functools import wraps

PY2 = sys.version[0] == '2'


# decorator for check-name
# Is this really useful...
def check_before(func):
    @wraps(func)
    def wrapped_func(self, *args, **kwargs):
        if not hasattr(self, 'name'):
            raise AttributeError("You must specity league/clue/player name first")
        func(self, *args, **kwargs)

    return wrapped_func


def print_league_news(news_dict):
    # 点击 q 退出，输入对应的链接查看网页内容
    pass


# relationship


league_transformat = {
    ('英超', 'Premier League', 'Premiere League', '英国', '英格兰'): 'EPL'
}

league_configure = {
    'EPL': {
        'rank_url': 'http://soccer.hupu.com/table/England.html',
        'news_url': 'http://soccer.hupu.com/england/'
    }
}

club_transformat = {
    ('manchester united', '曼联', '曼彻斯特联'): 'manutd'
}

club_url = {

}

football_url = {

}

connect_url = 'iamwanghz@gmail.com'
github_url = 'https://github.com/FBRank'

league_news_pattern = r'<h2><a class="f074" href="(.*?)".*?>(.*?)</a>'
