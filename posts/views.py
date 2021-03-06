from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from .models import Post
from .forms import PostForm

# Create your views here.
def list(request):
    # posts = Post.objects.all()
    posts = get_list_or_404(Post)
    context = {
        'posts' : posts,
    }
    return render(request, 'posts/list.html', context)
    
def detail(request, post_pk):
    context = {
        'post' : get_object_or_404(Post, pk=post_pk),
    }
    return render(request, 'posts/detail.html', context)
    
@login_required
def create(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect('posts:detail', post.pk)
    else:
        form = PostForm()
    context = {
        'form' : form,
    }
    return render(request, 'posts/postform.html', context)
    
@login_required
def update(request, post_pk):
    post = get_object_or_404(Post, pk=post_pk)
    if request.user != post.user:
        return redirect('posts:detail', post_pk)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save()
            return redirect('posts:detail', post_pk)
    else:
        context = {
            'form' : PostForm(instance=post)
        }
    return render(request, 'posts/postform.html', context)

@login_required
@require_POST
def delete(request, post_pk):
    post = get_object_or_404(Post, pk=post_pk)
    if request.user != post.user:
        return redirect('posts:detail', post_pk)
    post.delete()
    return redirect('posts:list')

@login_required
def like(request, post_pk):
    post = get_object_or_404(Post, pk=post_pk)
    if request.user in post.like_users.all():
        post.like_users.remove(request.user)
    else:
        post.like_users.add(request.user)
    return redirect('posts:list')