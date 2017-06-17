import tweepy
from credentials import *
import time

# Set up your authorisations
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
api = tweepy.API(auth)

followers = []
#follow POTUS friends
def pull_followers():
    #pull = api.followers('realDonaldTrump', -1)
    # for user in api.followers('realDonaldTrump', -2):
    #     followers_id = user.id
    #     #screen_name = user.screen_name
    #     followers.append(followers_id) #, screen_name) #print(user.id)
    # return(followers)
    users = tweepy.Cursor(api.followers, id ='realDonaldTrump').items()

    while True:
        try:
            user = next(users)
        except tweepy.TweepError:
            time.sleep(60*15)
            user = next(users)
        except StopIteration:
            break
        print(user.id)

    # for user in tweepy.Cursor(api.followers, id ='realDonaldTrump').items():
    #     print(user.id)

### Homework ####
# How do we make this slower so we don't get kicked off the API?
# Pull in followers in a small enough batches not to get the 429
# Put followers into another CSV so that the bot can check over them

##########################
# making friends to troll
#
# def friendly():
#     for follower in followers:
#     api.create_friendship(follower)
