# RedditStream Bot
This started as the [Heroku "python-gettting-started" project](https://devcenter.heroku.com/articles/getting-started-with-python) - check it out. See article for details getting the project running, setting up the db, and generally deploying to heroku.

This bot was built for collecting gamethreads in a subreddit [/r/reddit_stream](https://www.reddit.com/r/reddit_stream/) for use in my iOS app, [RedditStream](https://itunes.apple.com/us/app/stream-for-reddit/id1215001791?ls=1&mt=8)

H/T https://github.com/vishnumad/gamethread-scraper. Although on the exterior it essentially does the same thing, this repo has a backend to store the game thread meta data (so you don't duplicate post- he had an alternative implementation), and adds the capability to tweet the thread including a link to the app.
