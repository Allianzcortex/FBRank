# -*- coding:utf-8 -*-
import sys
from functools import wraps

PY2 = sys.version[0] == '2'


# decorator for check-name
# Is this really useful...
def check_before(func):
    @wraps(func)
    def wrapped_func(self, *args, **kwargs):
        if not hasattr(self, name):
            raise AttributeError("You must specity league/clue/player name first")
        func(self, *args, **kwargs)

    return wrapped_func


# relationship

league_url = {
    'permierleage': {
        'base_url': 'https://www.premierleague.com',
        'rank': 'tables'
    }
}

league_transformat = {
    ['manchester united', '曼联', '曼彻斯特联']: 'manutd'
}

club_url = {

}

football_url = {

}

connect_url = 'iamwanghz@gmail.com'
github_url = 'https://github.com/FBRank'
