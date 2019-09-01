import tweepy
from credentials import *
import random
print(tweepy.__version__)
# from requests.exceptions import Timeout, ConnectionError
# from requests.packages.urllib3.exceptions import ReadTimeoutError, ProtocolError
# import time

# logs into the acc
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
api = tweepy.API(auth)

# checks authentication
try:
    api.verify_credentials()
    print("Authentication OK")
except BaseException as e:
    print(e.reason)

# lines = open('NCT_bot.txt').read().splitlines() # splits the lines of the txt file with all the links of the songs

# tweet_ids = [] # list of ids of tweets that @ the acc

for tweet in tweepy.Cursor(api.search, q='@NCTsongbot').items(): # searches for any tweet that includes '@NCTsongbot'
    # tweet_ids.append($tweetID) # adds the id of the tweet the bot replied to to the list of ids
    print("Found tweet by:@" + tweet.user.screen_name)
    break
    # # searches for all tweets that reply to the user that mentioned the bot
    # for tweet in tweepy.Cursor(api.search, q ="to:$tweeterusername", sinceID = $tweetID):
    #     if in_reply_to_status_id_str = $tweetID:
    #         print("Already replied to:@" + tweet.user.screen_name)
    #     else: # tweets at the user a link/line chosen randomly from the txt file
    #         api.update_status("@" + tweet.user.screen_name + " " + random.choice(lines))
    #         print("responded to @" + tweet.user.screen_name)


# errors
    # except (tweepy.TweepError, tweepy.RateLimitError) as e:
    #     print(e.reason)
    #     time.sleep(5)
    #     continue
    # except (Timeout, ssl.SSLError, ConnectionError, ReadTimeoutError, ProtocolError) as exc:
    #     continue

# in terminal
# to keep bot going when laptop off
# nohup python3 bot.py &
# when recieve a string of numbers
# logout
# stop it with kill *numbers*

# class MyStreamListener(tweepy.StreamListener):
#
#     def on_status(self, status):
#         print(status.text)

# myStreamListener = MyStreamListener()
# myStream = tweepy.Stream(auth = api.auth, listener=myStreamListener)
