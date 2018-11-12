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
from .models import Course,CourseResourse,Lesson,Video

class CourseAdmin(object):
    list_display = ['name', 'desc', 'detail','degree','learn_time','studens','fav_nums','image','click_nums','add_time']
    search_fields =['name', 'desc', 'detail','degree','studens']
    list_filter = ['name', 'desc', 'detail','degree','learn_time','studens','fav_nums','image','click_nums','add_time']

class CourseResourseAdmin(object):
    list_display = ['course', 'name','download','add_time']
    search_fields = ['course', 'name','download']
    list_filter = ['course', 'name','download','add_time']

class LessonAdmin(object):
    list_display = ['course', 'name','add_time']
    search_fields = ['course', 'name']
    list_filter = ['course', 'name','add_time']

class VideoAdmin(object):
    list_display = ['lesson', 'name','add_time']
    search_fields = ['lesson', 'name']
    list_filter = ['lesson', 'name','add_time']

xadmin.site.register(Course,CourseAdmin)

xadmin.site.register(Lesson,LessonAdmin)
xadmin.site.register(Video,VideoAdmin)
xadmin.site.register(CourseResourse,CourseResourseAdmin)