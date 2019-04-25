from django.shortcuts import render, redirect, get_object_or_404
from .models import Post
from .forms import PostForm

# Create your views here.
def list(request):
    posts = Post.objects.all()
    context = {
        'posts' : posts,
    }
    return render(request, 'posts/list.html', context)
    
def detail(request, post_pk):
    context = {
        'post' : get_object_or_404(Post, pk=post_pk),
    }
    return render(request, 'posts/detail.html', context)
    
def create(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save()
            return redirect('posts:list')
            # return redirect('posts:detail', post.pk)
    else:
        form = PostForm()
    context = {
        'form' : form,
    }
    return render(request, 'posts/create.html', context)