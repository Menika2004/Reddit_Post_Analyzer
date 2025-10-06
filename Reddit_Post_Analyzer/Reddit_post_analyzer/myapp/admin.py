from django.contrib import admin
from .models import RedditPost

# Register your models here.
class RedditPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'subreddit', 'score', 'comments', 'created')

admin.site.register(RedditPost, RedditPostAdmin)

