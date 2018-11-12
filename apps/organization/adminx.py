# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     adminx
   Description :
   Author :       seven
   date：          2018/11/12
-------------------------------------------------
   Change Activity:
                   2018/11/12:
-------------------------------------------------
"""
__author__ = 'seven'
import xadmin
from .models import CityDict,CourseOrg,Teacher

class CityDictAdmin(object):
    list_display = ['name', 'desc', 'add_time']
    search_fields = ['name', 'desc']
    list_filter = ['name', 'desc', 'add_time']

class CourseOrgAdmin(object):
    list_display = ['name', 'desc', 'click_num', 'fav_num', 'image','address','city']
    search_fields = ['name', 'desc', 'click_num', 'fav_num', 'image','address','city']
    list_filter = ['name', 'desc', 'click_num', 'fav_num', 'image','address','city']

class TeacherAdmin(object):
    list_display = ['name', 'work_years', 'work_company', 'work_position', 'points','click_num','fav_num','add_time']
    search_fields = ['name', 'work_years', 'work_company', 'work_position', 'points','click_num','fav_num']
    list_filter = ['name', 'work_years', 'work_company', 'work_position', 'points','click_num','fav_num','add_time']

xadmin.site.register(CityDict,CityDictAdmin)
xadmin.site.register(Teacher,TeacherAdmin)
xadmin.site.register(CourseOrg,CourseOrgAdmin)