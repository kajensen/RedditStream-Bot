import twitter
import os

api = twitter.Api(consumer_key=os.environ['TWITTER_CONSUMER_KEY'],
                      consumer_secret=os.environ['TWITTER_CONSUMER_SECRET'],
                      access_token_key=os.environ['TWITTER_ACCESS_TOKEN_KEY'],
                      access_token_secret=os.environ['TWITTER_ACCESS_TOKEN_SECRET'])

def tweet(thread, branch_url):
    tweet_id = None
    try:
        max_length = 136-len(branch_url)
        title = "[r/{0}] {1}".format(thread.subreddit, thread.title)
        truncated_title = (title[:max_length] + "...") if len(title) > max_length else title
        tweet = "{0} {1}".format(truncated_title, branch_url)
        status = api.PostUpdate(tweet)
        tweet_id = status.id
    except Exception as inst:
        print(type(inst))
        print(inst.args)
        print(inst)
        pass
    return tweet_id
