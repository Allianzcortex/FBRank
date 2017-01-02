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



# relationship


league_transformat = {
    ('英超', 'Premier League', 'Premiere League', '英国', '英格兰'): 'EPL',
    ('德甲', 'Bundesliga', 'Bunde', '德国'): 'Bunde',
    ('西甲', 'Liga BBva', '西班牙'): 'La Liga',
    ('意甲', 'Serie A', '意大利'): 'Serie A'
}

league_configure = {
    'EPL': {
        'rank_url': 'http://soccer.hupu.com/table/England.html',
        'news_url': 'http://sports.sina.com.cn/g/premierleague/'
    },
    'Bunde': {
        'rank_url': 'http://soccer.hupu.com/table/Germany.html',
        'news_url': 'http://sports.sina.com.cn/g/bundesliga/'
    },
    'La Liga': {
        'rank_url': 'http://soccer.hupu.com/table/Spain.html',
        'news_url': 'http://sports.sina.com.cn/g/laliga/'
    },
    'Serie A': {
        'rank_url': 'http://soccer.hupu.com/table/Italy.html',
        'news_url': 'http://sports.sina.com.cn/g/seriea/'
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
