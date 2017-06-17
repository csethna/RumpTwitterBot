#Getting some tweets
import tweepy
import time
from credentials import *
import datetime
import pytz
import log
import csv
import tweet_cache

def get_tweets():
    #Get the auth stuff in order
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
    api = tweepy.API(auth)

	tweets = api.user_timeline(screen_name = 'realDonaldTrump', count=5, include_rts= True, parser=tweepy.parsers.JSONParser())
    trimmed_tweets = tweet_cache.cache_and_trim('tweet_ids.csv', tweets)

    return trimmed_tweets
