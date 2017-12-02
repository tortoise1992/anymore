from django.shortcuts import render

# Create your views here.

from blog.models import User

def index(req):
    return render(req,'index.html')