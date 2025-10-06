import praw
from datetime import datetime
import pytz
from myapp.models import RedditPost  # import your model

# Initialize Reddit API
reddit = praw.Reddit(
    client_id='gn8eotCK7mq6JfE_C4dGOg',
    client_secret='evg6bXyg6G90ptBsfRwYEGR1Qma3KQ',
    user_agent='script:Post Analyzer:v1.0 (by /u/Ok_Hedgehog9032)'
)

def fetch_subreddit_data(subreddit_name, limit=20):
    subreddit = reddit.subreddit(subreddit_name)
    posts = []

    for post in subreddit.hot(limit=limit):
        # Convert timestamp to timezone-aware datetime object
        created_time = datetime.utcfromtimestamp(post.created_utc).replace(tzinfo=pytz.UTC)

        # Save to database
        RedditPost.objects.create(
            subreddit=subreddit_name,
            title=post.title,
            score=post.score,
            comments=post.num_comments,
            created=created_time,
            url=post.url
        )

        # Append for template rendering
        posts.append({
            'title': post.title,
            'score': post.score,
            'comments': post.num_comments,
            'created': created_time.strftime('%Y-%m-%d %H:%M:%S'),  # ✅ readable format
            'url': post.url
        })

    return posts
