# Some basic Twitter bot script fun.

import tweet
import create_image
import get_tweets
import clean_up_imgs

tweets = get_tweets.get_tweets()

create_image.imagify_tweet(tweets)

tweet.send(tweets)

clean_up_imgs.clean()