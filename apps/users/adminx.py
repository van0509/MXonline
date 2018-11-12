# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     adminx.py
   Description :
   Author :       seven
   date：          2018/11/11
-------------------------------------------------
   Change Activity:
                   2018/11/11:
-------------------------------------------------
"""
__author__ = 'seven'

import xadmin
from .models import EmailVerifyRecord, Banner
from xadmin import views


class BaseSetting(object):
    enable_themes = True
    use_bootswatch = True


class GlobalSettings(object):
    site_title = '幕学后台管理系统'
    site_footer = '幕学在线网'
    menu_style = 'accordion'


class EmailVerifyRecordAdmin(object):
    list_display = ['code', 'email', 'sned_type', 'send_time']
    search_fields = ['code', 'email', 'sned_type', 'send_time']
    list_filter = ['code', 'email', 'sned_type', 'send_time']


class BannerAdmin(object):
    list_display = ['title', 'image', 'url', 'index', 'add_time']
    search_fields = ['title', 'image', 'url', 'index']
    list_filter = ['title', 'image', 'url', 'index', 'add_time']


xadmin.site.register(EmailVerifyRecord, EmailVerifyRecordAdmin)
xadmin.site.register(Banner, BannerAdmin)
xadmin.site.register(views.BaseAdminView, BaseSetting)
xadmin.site.register(views.CommAdminView, GlobalSettings)
