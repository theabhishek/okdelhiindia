from django.shortcuts import render
from posts.models import Post
from subreddits.models import Subreddit

def home(request):
    posts = Post.objects.all().order_by('-created_at')
    subreddits = Subreddit.objects.all().order_by('-created_at')[:5]
    
    context = {
        'posts': posts,
        'subreddits': subreddits,
    }
    
    return render(request, 'core/home.html', context)

def about(request):
    return render(request, 'core/about.html')

def terms(request):
    return render(request, 'core/terms.html')

def privacy(request):
    return render(request, 'core/privacy.html') 