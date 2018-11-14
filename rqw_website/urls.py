"""rqw_website URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
from Article.views import *
from Article.views import AddCommentView
urlpatterns = [
    # 1.实现博客的展示, yi初识python

    # 2,实现列表详情页
    # 3,实现博客分页功能
    # 4.实现博客评论功能
    url(r'^blog',blog_url_view,name='blog'),
    url(r'^b_detail$',blogdetail_url_view,name='blog_detail'),
    url(r'^homepage', homePage, name='home'),
    url(r'^admin/', admin.site.urls),
    url(r'^ckeditor', include('ckeditor_uploader.urls')),
    # url(r'^add_comment',AddCommentView.as_view()),   #博客评论url
    url('^signin',sigin,name='sign')

    # url(r'^test',test),
]
