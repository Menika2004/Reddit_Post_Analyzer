from django.shortcuts import render, redirect
import json
from myapp.reddit_utils import fetch_subreddit_data
from myapp.models import RedditPost

def home(request):
    """Display the home page with search form and instructions."""
    return render(request, 'myapp/home.html')

def analyze(request):
    """Handle subreddit POST and show results in results.html."""
    if request.method == 'POST':
        subreddit = request.POST.get('subreddit')

        if not subreddit:
            return render(request, 'myapp/home.html', {'error': 'Subreddit name is required!'})

        # Fetch posts and display them (already saved in DB inside reddit_utils)
        data = fetch_subreddit_data(subreddit)

        return render(request, 'myapp/results.html', {
            'data': data,
            'json_titles': json.dumps([d['title'] for d in data]),
            'json_scores': json.dumps([d['score'] for d in data])
        })

    return redirect('home')  # If not POST, go back to home

def saved_posts(request):
    """Display saved posts from database."""
    subreddit = request.GET.get('subreddit')
    if subreddit:
        posts = RedditPost.objects.filter(subreddit__iexact=subreddit).order_by('-created')[:50]
    else:
        posts = RedditPost.objects.all().order_by('-created')[:50]

    return render(request, 'myapp/saved_posts.html', {'posts': posts})
