import tweepy
import json
import re
from credentials import *

# Set up your authorisations
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
api = tweepy.API(auth)

for result in api.search(q="@realTrumpyBot"):
    print(result.text)
    print(result.user.screen_name)
    #print(result['user'])

# data = api.search(q="@realTrumpyBot")
# # data.values()[1][2]['text']
#
# print(data)

# html_filter = re.compile('<[^<]+?>')

# def mentions():
#     mentions = api.mentions_timeline(params = {
#     'screen_name' : '' ,
#     'text' : ''
#     }
#     )
#
#     json.loads(mentions)
#
#     complete_response = response['screen_name'][0]['text']
#
#     print(complete_response)
#
#     return complete_response



# # Set up API call
# api = tweepy.API(auth, parser = tweepy.parsers.JSONParser())
#
# # Set search query
# searchquery = '@realTrumpyBot -filter:mentions'
#
# # Make call to API
# data = api.search(q = searchquery, count = 100, lang = 'en', result_type = 'mixed')
#
# print(data)
