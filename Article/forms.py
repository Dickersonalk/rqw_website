#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/2/7 11:52
# @Author  : QiWei.Ren
# -*- coding: utf-8 -*-
from django import forms
from django.contrib.admin import widgets
from Article.models import Comment
class Commentform(forms.ModelForm):
    """增加评论"""
    class Meta:
        model=Comment
        fields=['name','content','blog']

class PostForm(forms.Form):
    """增加时间插件"""
    date = forms.DateTimeField(widget=widgets.AdminDateWidget(),label=u"时间")

