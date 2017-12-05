from django.shortcuts import render,get_object_or_404
import markdown
# Create your views here.

from blog.models import User,Post

def index(req):
    # article_list=Article.objects.all()
    post_list=Post.objects.all()
    return render(req,'blog/index.html',{'post_list':post_list})


def detail(req,pk):
    post=get_object_or_404(Post,pk=pk)
    post.body = markdown.markdown(post.body,
                                  extensions=[
                                      'markdown.extensions.extra',
                                      'markdown.extensions.codehilite',
                                      'markdown.extensions.toc',
                                  ])
    return render(req,'blog/detail.html',{'post':post})

def archives(req,year,month):
    post_list=Post.objects.filter(
        create_time__year=year,
        # create_time__month=month
        author_id=1
        # 无法按月查询就多保存一个字段
    ).filter().order_by('-create_time')
    print(year,month)
    return render(req,'blog/index.html',{'post_list':post_list})