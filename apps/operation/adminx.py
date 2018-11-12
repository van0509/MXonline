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

from .models import UserAsk,UserCourse,UserFavorite,UserMessage,CourseComments

class UseraskAdmin(object):
    list_display = ['name', 'mobile', 'course_name', 'add_time']
    search_fields = ['name', 'mobile', 'course_name']
    list_filter = ['name', 'mobile', 'course_name', 'add_time']

class UserCourseAdmin(object):
    list_display = ['user', 'course', 'add_time']
    search_fields = ['user', 'course']
    list_filter = ['user', 'course', 'add_time']
class UserFavoriteAdmin(object):
    list_display = ['user', 'fav_id', 'fav_type', 'add_time']
    search_fields = ['user', 'fav_id', 'fav_type']
    list_filter = ['user', 'fav_id', 'fav_type', 'add_time']
class UserMessageAdmin(object):
    list_display = ['user', 'message', 'add_time', 'has_read']
    search_fields = ['user', 'message', 'add_time']
    list_filter = ['user', 'message', 'add_time', 'has_read']
class CourseCommentsAdmin(object):
    list_display = ['user', 'course', 'add_time']
    search_fields = ['user', 'course']
    list_filter = ['user', 'course', 'add_time']

xadmin.site.register(UserAsk,UseraskAdmin)
xadmin.site.register(UserMessage,UserMessageAdmin)
xadmin.site.register(UserCourse,UserCourseAdmin)
xadmin.site.register(UserFavorite,UserFavoriteAdmin)
xadmin.site.register(CourseComments,CourseCommentsAdmin)