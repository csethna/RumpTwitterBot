# Some basic Twitter bot script fun.

import tweet
import create_image
import get_tweets
import clean_up_imgs
import mentions
import log


tweets = get_tweets.get_tweets()

if(len(tweets) > 0):

	create_image.imagify_tweet(tweets)
	tweet.send(tweets)
	clean_up_imgs.clean()

else:
	log.log("No tweets to tweet :(")

# mentions bro
mentions = mentions.get()

if(len(mentions) > 0):
	mentions.reply(mentions)

else:
	log.log("No mentions to tweet :(")
