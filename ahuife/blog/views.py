from django.shortcuts import render

# Create your views here.

from blog.models import User

def index(req):
    # article_list=Article.objects.all()
    return render(req,'index.html')


def detail(req,article_id):
    # article=Article.objects.get(id=article_id)
    return render(req,'detail.html')

def list(req):
    return render(req,'list.html')