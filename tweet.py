import tweepy, time
from credentials import *
import glob

def send(tweets):
	auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
	auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
	api = tweepy.API(auth)

	#get images that were generated
	images = glob.glob("trump_exec_order_*")
	print(images)

	for index, tweet in enumerate(tweets):
		api.update_with_media(images[index], "#TrollTrump")
		
