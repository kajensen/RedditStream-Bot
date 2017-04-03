from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.core import serializers

from .models import Thread

from gamethread_scraper import reddit_bot
from gamethread_scraper import twitter_bot
from gamethread_scraper import branch
import datetime
import time

import twitter
import os

# Create your views here.
def update(request):

    ts = reddit_bot.getThreads()
    threads = []
    for t in ts:
        defaults = {
            'subreddit': t.subreddit,
            'subreddit_id': t.subreddit_id,
            'author': t.author,
            'author_flair_text': t.author_flair_text,
            'title': t.title,
            'score': t.score,
            'num_comments': t.num_comments,
            'reddit_url': t.shortlink,
            'date_created_utc': t.created_utc
        }
        thread = None
        thread, created = Thread.objects.get_or_create(id = t.id, defaults = defaults)

        if created:
            branch_url = branch.createURL(thread)
            thread.branch_url = branch_url
            if os.environ.get('TWITTER_ENABLED', False):
                tweet_id = twitter_bot.tweet(thread, branch_url)
                thread.tweet_id = tweet_id
            if os.environ.get('REDDIT_ENABLED', False):
                reddit_id = reddit_bot.postThread(thread)
                thread.reddit_id = reddit_id

        thread.save()
        threads.append(thread)

    data_json = serializers.serialize("json", threads)
    return HttpResponse(data_json, content_type="application/json")

def get(request):
    lastThreeHours = datetime.datetime.utcnow() - datetime.timedelta(hours = 3)
    ts = time.mktime(lastThreeHours.timetuple())
    threads = Thread.objects.all().filter(date_created_utc__gt=ts)
    data_json = serializers.serialize("json", threads)
    return HttpResponse(data_json, content_type="application/json")
