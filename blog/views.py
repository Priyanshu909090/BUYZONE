from django.shortcuts import render
from django.shortcuts import HttpResponse
from .models import BlogPost


# Create your views here.
def index(request):
    blogpost = BlogPost.objects.all()
    param = {'blogpost': blogpost}
    return render(request, 'blog/index.html', param)


def blogpost(request, id):
    posts = BlogPost.objects.filter(blogpost_id=id)[0]

    return render(request, 'blog/blogpost.html', {'posts': posts})
