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

def list(req):
    return render(req,'list.html')