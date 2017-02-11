#Getting some tweets
import tweepy, time
from credentials import *
import datetime
from datetime import datetime
import pytz

def get_tweets():

	#Get the auth stuff in order
	auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
	auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
	api = tweepy.API(auth)

	tweets = api.user_timeline(screen_name = 'realDonaldTrump', count=20, include_rts= True, parser=tweepy.parsers.JSONParser())
	trimmed_tweets = []
	#Check whether this tweet occurred within the last minute
	for index, tweet in enumerate(tweets):
		created_at = datetime.strptime(tweet['created_at'], '%a %b %d %H:%M:%S %z %Y').replace(tzinfo=pytz.utc)
		current_time = datetime.utcnow().replace(tzinfo=pytz.utc)
		difference = (current_time - created_at).total_seconds()


		if (difference <= 60):
			trimmed_tweets.append(tweet)

	return trimmed_tweets