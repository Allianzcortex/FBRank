# # -*- coding:utf-8 -*-
# """
# Use For All Club
# One CLub should hava attributes as folowing:
# - name
# - create_time
# - Court
# - coach
# - belog_league
# """
#
# from FBRank.utils.utils import league_transformat, check_before
# from FBRank.utils.Exceptions import IllegalNameException
#
#
# class Club(object):
#     def __init__(self, intro_name):
#         self.name = self._get_name(intro_name)
#         self.website = self._get_website(self.name)
#
#     def _get_name(self, name):
#         temp_name = name.lower()
#         for leaguname_list in league_transformat.keys():
#             if temp_name in leaguname_list:
#                 return league_url.get(temp_name)
#
#         raise IllegalNameException(name)
#
#     @check_before
#     def _get_website(self, name):
#         return league_url.get(name).get('base_url')
