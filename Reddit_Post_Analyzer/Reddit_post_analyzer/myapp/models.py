from django.db import models

class RedditPost(models.Model):
    title = models.TextField()
    score = models.IntegerField()
    comments = models.IntegerField()
    created = models.DateTimeField()
    url = models.URLField()
    subreddit = models.CharField(max_length=100)

    def __str__(self):
        return self.title
