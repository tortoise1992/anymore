from django.shortcuts import render,get_object_or_404,redirect
from blog.models import Post

from .models import Comments
from .forms import CommentForm
# Create your views here.


def post_comment(req,post_id):
    post=get_object_or_404(Post,pk=post_id)
    print(post)
    if req.method=='POST':
        form=CommentForm(req.POST)
        if form.is_valid():
            comment=form.save(commit=False)
            comment.post=post
            comment.save()
            return redirect(post)

        else:
            comment_list = Comments.objects.filter(post=post)
            context = {'post': post,
                       'form': form,
                       'comment_list': comment_list
                       }
            return render(request, 'blog/detail.html', context=context)

    return redirect(post)