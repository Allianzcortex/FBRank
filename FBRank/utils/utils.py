# -*- coding:utf-8 -*-
import sys
from functools import wraps

# from .exceptions import NotSupprotedYetException
# If used , it will cause circulation import
"""
File "/home/hzcortex/FBRank/FBRank/parse/League.py", line 13, in <module>
    from FBRank.utils.exceptions import IllegalArgumentException, NotSupprotedYetException
  File "/home/hzcortex/FBRank/FBRank/utils/exceptions.py", line 2, in <module>
    from .utils import github_url, connect_url
  File "/home/hzcortex/FBRank/FBRank/utils/utils.py", line 5, in <module>
    from .exceptions import NotSupprotedYetException
ImportError: cannot import name 'NotSupprotedYetException'

"""

PY2 = sys.version[0] == '2'


# decorator for check-name
# For Club Check
def check_before(attr='name'):
    from .exceptions import NotSupprotedYetException
    def wrapped_func(func):
        @wraps(func)
        def wrapped(self, *args, **kwargs):
            # print(func.__class__.__name__)
            if (getattr(self, attr).lower() not in club_transformat.keys()):
                raise NotSupprotedYetException
            return func(self, *args, **kwargs)

        return wrapped

    return wrapped_func


# relationship

EPL_League_transformat = {
    "利物浦":"Liverpool",
    "曼城":"Man City",
    "热刺":"Spurs",
    "阿森纳":"Arsenal",
    "曼联":"Man Utd",
    "维拉":"Aston Villa",
    "诺维奇":"Norwich City",
    "谢菲联":"Sheffield",
    "切尔西":"Chelsea",
    "沃特福德":"Watford",
    "狼队":"Wolves",
    "西汉姆":"West Ham",
    "伯恩茅斯":"AFC Bournemouth",
    "埃弗顿":"Everton",
    "莱斯特":"Leicester",
    "水晶宫":"Crystal Palace",
    "伯恩利":"Burnley",
    "纽卡斯尔":"Newcastle",
    "布莱顿":"Brighton",
    "卡迪夫城":"Cardiff",
    "南安普顿":"Southampton",
    "富勒姆":"Fulham",
    "哈德斯菲尔德":"Huddersfield",
    "卢顿":"Luton Town",
    "巴恩斯利":"Barnsley",
    "桑德兰":"Sunderland",
    "朴茨茅斯":"Portsmouth",
    "查尔顿":"Charlton Athletic",
    "唐卡斯特":"Doncaster Rovers",
    "彼得堡联":"Peterborough United",
    "福利特":"Fleetwood Town",
    "布莱克浦":"Blackpool",
    "考文垂":"Coventry City",
    "伯顿":"Burton Albion",
    "威科姆":"Wycombe Wanderers",
    "普利茅斯":"Southend United",
    "斯肯索普":"Plymouth Argyle",
    "南安联":"Accrington Stanley",
    "阿克宁顿":"Scunthorpe United",
    "吉灵汉姆":"Gillingham",
    "沃尔索尔":"Walsall",
    "牛津联":"Shrewsbury Town",
    "什鲁斯":"Oxford United",
    "罗奇代尔":"Bristol Rovers",
    "布流浪":"Rochdale",
    "布拉德福":"Bradford City",
    "温布尔登":"AFC Wimbledon"
}

league_transformat = {
    ('英超', 'EPL','Premier League', 'Premiere League', '英国', '英格兰'): 'EPL',
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
