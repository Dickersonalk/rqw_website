from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
# 文章  : 作者,文章名称,发表日期,阅读次数,图片,文章类型,文章内容 ,文章描述
# 图片  : 图片名称,图片地址 外jian
# 类型  : 类型名称,类型描述
# Create your models here.
class Type(models.Model):
    name=models.CharField(max_length=100,verbose_name="类型名称")
    description=RichTextUploadingField(verbose_name="类型描述")

    def __str__(self):
        return self.name

class Article(models.Model):
    title=models.CharField(max_length=100,verbose_name="文章标题")
    author=models.CharField(max_length=100,verbose_name="文章作者")
    content=models.TextField(verbose_name="正文",default='')
    # content=models.Field(verbose_name="文章内容")
    description= models.CharField(max_length=32,verbose_name="文章描述")
    post_date=models.DateField(verbose_name="发表日期")
    pic=models.ImageField(upload_to="images",verbose_name="图片")
    num=models.IntegerField(verbose_name="阅读次数")
    types=models.ForeignKey(to="Type",to_field="id")

    def __str__(self):
        return self.title

class Picture(models.Model):
    title= models.CharField(max_length=32,verbose_name="图片名称")
    src=models.ImageField(upload_to="images",verbose_name="图片链接")
    types= models.ForeignKey(to="Type",to_field="id")

    def __str__(self):
        return self.title

class Comment(models.Model):
    "实现评论功能"
    name = models.CharField(verbose_name='姓名', max_length=20, default='佚名')
    content = models.CharField(verbose_name='内容', max_length=300)
    create_time = models.DateTimeField(verbose_name='创建时间', auto_now_add=True)
    blog = models.ForeignKey(to='Article',to_field='id',verbose_name='博客')

    # class Meta:
    #     verbose_name = '博客评论'
    #     verbose_name_plural = verbose_name

    def __str__(self):
        return self.content[:10]