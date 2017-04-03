from django.db import models

class Thread(models.Model):
    id = models.CharField(max_length=500, primary_key=True)
    date_created_utc = models.IntegerField(null=True)
    subreddit = models.CharField(max_length=500, null=True)
    subreddit_id = models.CharField(max_length=500, null=True)
    reddit_url = models.CharField(max_length=500, null=True)
    reddit_id = models.CharField(max_length=500, null=True)
    branch_url = models.CharField(max_length=500, null=True)
    tweet_id = models.CharField(max_length=500, null=True)
    author = models.CharField(max_length=500, null=True)
    author_flair_text = models.CharField(max_length=500, null=True)
    title = models.CharField(max_length=500, null=True)
    score = models.IntegerField(default=0)
    num_comments = models.IntegerField(default=0)
