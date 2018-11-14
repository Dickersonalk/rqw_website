# from django.shortcuts import render,HttpResponse,render_to_response
# from Article.models import Article
# Create your views here.
from django.shortcuts import render,render_to_response
from Article.models import Article,Type,Picture,Comment
from django.http import HttpResponse
from Article.forms import Commentform,PostForm
from django.views import View
import markdown

def sigin(requset):
    return render_to_response("signin.html")

def homePage(request):
    return  render_to_response("home_page/home.html")




def blogdetail_url_view(request):

    article= Article.objects.all()
    current_id =int(request.GET.get('id'))
    Articles_detail = Article.objects.get(id=current_id)
    Articles_detail.content = markdown.markdown(Articles_detail.content)
    # 0     1234567       8   youbiao 0-7    id 1-8

    previous= current_id-1   #上一页 = 当前也-1
    next =current_id+1       #下一页 =当前也+1
    count = article.count()
    try:
        next_title = article[next - 1]
    except Exception as e:
        print(e)

    try:
        previous_title = article[previous - 1]
    except AssertionError:
        print(AssertionError)

    while current_id == count:
        next_id=count
        next_title = article[next_id - 1]
        break
    while current_id == 1:
        previous_id= current_id
        previous_title = article[previous_id - 1]
        break

    return render(request, 'blog/b_detail.html',
                  {'artic': Articles_detail,
                  'previous_title':previous_title,
                  'previous':previous,'next_title':next_title,
                  'next':next,'count':count})

def blog_url_view(request):
    """博客,博客详情页以及类型展示"""
    article=Article.objects.all()
    Types = Type.objects.all()
    # print(Articles[0].id)
    detail=[]
    form = PostForm(request.POST)   #时间插件
    return render(request,'blog/blog.html',{'Articless':article,'Typess':Types,'form':form})
#



#
# def Type_url(request):
#
#     return render(request,'blog/blog.htmlo.html',{'Typess':Types})


class AddCommentView(View):
    "评论url"
    def post(self,request):
        comment_form=Commentform(request.POST)
        if comment_form.is_valid():
            comment_form.save()
            return HttpResponse('{"status":"success"}',content_type='application/json')
        else:
            return HttpResponse('{"status":"fail"}',content_type='application/json')

def test(request):
    return render(request,'test1.html')