from django.shortcuts import render,get_object_or_404
import markdown
from django.urls import reverse
from comments.forms import CommentForm
from comments.models import Comments
# Create your views here.

from blog.models import User,Post,Category

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

    # 记得在顶部导入 CommentForm
    form = CommentForm()
    # 获取这篇 post 下的全部评论
    comment_list = Comments.objects.filter(post=post)
    # 将文章、表单、以及文章下的评论列表作为模板变量传给 detail.html 模板，以便渲染相应数据。
    context = {'post': post,
               'form': form,
               'comment_list': comment_list
               }
    return render(req,'blog/detail.html',context=context)

def archives(req,year,month):
    post_list=Post.objects.filter(
        create_time__year=year,
        # create_time__month=month
        # author_id=1
        # 无法按月查询就多保存一个字段
    ).filter().order_by('-create_time')
    print(year,month)
    return render(req,'blog/index.html',{'post_list':post_list})

def category(req,pk):
    cate=get_object_or_404(Category,pk=pk)
    post_list=Post.objects.filter(category=cate).order_by('-create_time')
    return render(req, 'blog/index.html', context={'post_list': post_list})