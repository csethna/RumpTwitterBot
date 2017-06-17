import tweepy
from credentials import *
import json

# Set up your authorisations
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
api = tweepy.API(auth)

#follow POTUS friends
def pull_followers():
    pull = api.followers('realDonaldTrump')
    for user in pull:
        print(user.id)
