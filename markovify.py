import markovify
import tweepy
from credentials import *
import csv

#Get the auth stuff in order
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
api = tweepy.API(auth)

#Function to get the body of the Tweet for Markov Processing
def get_corpus():

    tweet_texts = api.user_timeline(screen_name = 'realDonaldTrump', count=5, include_rts= True, parser=tweepy.parsers.JSONParser())
    # return tweet_texts #this part works

    for tweet_text in tweet_texts:
        corpus_tweet_text = {}    # $$money shot
        corpus_tweet_text.append(tweet_text.text)

        #Write to CSV
        # corpus_tweet_text dictionary

        markov_csv = open("markov.csv", "wb")
        dw = csv.DictWriter(markov_csv,corpus_tweet_text.text())
        dw.writerow(markov_csv)
        markov_csv.close()


#### Markov Process #### ----> NewlineText error probably due to error with csv portion.
#
# # Get raw text as string.
# with open('markov.csv') as f:
#     text = f.read()
#
# # Build the model.
# text_model = markovify.NewlineText(text) # NewlineText requires each tweet to be on a new line in the csv.
#
# # Print five randomly-generated sentences
# for i in range(5):
#     print(text_model.make_sentence())
#
# # Print three randomly-generated sentences of no more than 140 characters
# for i in range(3):
#     print(text_model.make_short_sentence(140))
