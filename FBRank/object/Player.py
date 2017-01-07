# -*- coding:utf-8 -*-


class Player(object):
    def __init__(self, intro_name):
        self.name = intro_name

    def __repr__(self):
        return '<Player {}>'.format(self.name)
