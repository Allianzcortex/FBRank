# -*- coding:utf-8 -*-
from .utils import github_url, connect_url


class FBRankException(Exception):
    """ Base Exception FOr FBRank Project
    """
    exit_code = 1

    def __init__(self, message):
        pass

    def __repr__(self):
        return "This is Base Exception"


class IllegalArgumentException(FBRankException):
    """Use When argument is illegal
    """


class IllegalNameException(FBRankException):
    """use when provide name is not illegal
    """

    def __repr__(self, name):
        message = "Sorry What your input {name} can't be recongnized,you can seed an email to the" \
                  "{mail},or send one PR to the {github}".format(name=name, mail=connect_url, github=github_url)
        return message
