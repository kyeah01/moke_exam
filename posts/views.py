from django.shortcuts import render
from .models import Post
from .forms import PostForm

# Create your views here.
def list(request):
    posts = Post.objects.all()
    context = {
        'posts' : posts,
    }
    return render(request, 'posts/list.html', context)
    
