import datetime
import praw
import os

reddit = praw.Reddit(client_id=os.environ['REDDIT_CLIENT_ID'],
                     client_secret=os.environ['REDDIT_CLIENT_SECRET'],
                     user_agent=os.environ['REDDIT_USER_AGENT'],
                     username=os.environ['REDDIT_USERNAME'],
                     password=os.environ['REDDIT_PASSWORD'])

def pattern_in_title(m_title, m_list):
    for pattern in m_list:
        if pattern in m_title:
            return True
    return False

def postThread(thread):
    thread_id = None
    try:
        title = "{0} (x-post /r/{1})".format(thread.title, thread.subreddit)
        subreddit = reddit.subreddit('reddit_stream')
        submission = subreddit.submit(title, url=thread.reddit_url)
        thread_id = submission.id
    except Exception as inst:
        print(type(inst))
        print(inst.args)
        print(inst)
        pass
    return thread_id

def getThreads():
	game_threads = []

	# Match and discard lists
	match_list = ["Match Thread",
				  "Race Thread",
				  "Race Discussion",
				  "GAME THREAD",
				  "Game Thread"]

	discard_list = ["Post Match",
					"Post-Match",
					"Pre Match",
					"Pre-Match",
					"Post Race",
					"Post-Race",
					"Pre Race",
					"Pre Game",
					"Pre-Game",
					"Post Game",
					"POST GAME",
					"Post-Game"]

	try:
		sports_multi = reddit.multireddit('reddit_stream', 'sports')
		posts = sports_multi.new(limit=100)

		for submission in posts:
			s_title = submission.title

			if pattern_in_title(s_title, match_list) and not pattern_in_title(s_title, discard_list):
				game_threads.append(submission)

	except Exception as inst:
		print(type(inst))
		print(inst.args)
		print(inst)
		pass

	return game_threads
