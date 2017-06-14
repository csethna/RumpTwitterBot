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
	tweets = api.user_timeline(screen_name = 'realDonaldTrump', count=5, include_rts= True, parser=tweepy.parsers.JSONParser())
	trimmed_tweets = []
	used_ids = []

	with open('tweet_ids.csv', "r") as id_file:
		reader = csv.reader(id_file, delimiter = ',')
		used_ids = list(reader)[0]

	for index, tweet in enumerate(tweets):
		log.log(' '.join(('The tweets to check...', str(tweet['id']))))
		if tweet['id_str'] not in used_ids:
			trimmed_tweets.append(tweet)
			log.log(' '.join(('Adding...', tweet['id_str'])))

	log.log(' '.join(('Number of tweets to post:', str(len(trimmed_tweets)))))
	tweet_ids = [tweet['id_str'] for tweet in tweets]

	with open('tweet_ids.csv', 'w') as myfile:
	    wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
	    wr.writerow(tweet_ids)

	return trimmed_tweets
