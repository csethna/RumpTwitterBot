#Getting some tweets
import tweepy, time
from credentials import *
import datetime
from datetime import datetime
import pytz
import log
import csv

def get_tweets():
	#Get the auth stuff in order
	auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
	auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
	api = tweepy.API(auth)
	tweets = api.user_timeline(screen_name = 'realDonaldTrump', count=2, include_rts= True, parser=tweepy.parsers.JSONParser())
	trimmed_tweets = []

	#Check whether this tweet occurred within the last minute
	for index, tweet in enumerate(tweets):
		created_at = datetime.strptime(tweet['created_at'], '%a %b %d %H:%M:%S %z %Y').replace(tzinfo=pytz.utc)
		current_time = datetime.utcnow().replace(tzinfo=pytz.utc)
		difference = (current_time - created_at).total_seconds()

		log.log(' '.join(('The tweets to check...', str(tweet['id']))))

		if (difference <= 90):
			with open('tweet_ids.csv', "r+") as id_file:
				ids = csv.reader(id_file, delimiter = ',')
				used = False
				for row in ids:
					for field in row:
						if str(tweet['id']) in field:
							used = True
							log.log(' '.join(('found used tweet ', str(tweet['id']))))
					log.log(' '.join(('Already tweeted = ', str(used))))
					if used == False:
						trimmed_tweets.append(tweet)
						log.log("Going to tweet: " + tweet['text'])
						id_file.write(str(tweet['id']) + ",")

	return trimmed_tweets
