import tweepy
from credentials import *
import glob
import tweet_cache

# Set up your authorisations
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
api = tweepy.API(auth)

# wrong = Image.open('wrong.jpg')
wrong = glob.glob("wrong.gif")

results = api.search(q="@realTrumpyBot", count = 50)

for result in results:
    mention_text = result.text
    goofy_user = result.user.screen_name
    mention_id = result.id
    tweet_string = "@" + goofy_user + " WRONG!"

mention_tweets = tweet_cache.cache_and_trim('mention_ids.csv', results)

for tweet in mention_tweets:
    api.update_with_media(wrong[0], tweet_string, in_reply_to_status_id = mention_id)
