import tweepy # version 3.8.0
from credentials import *
import random
# from requests.exceptions import Timeout, ConnectionError
# from requests.packages.urllib3.exceptions import ReadTimeoutError, ProtocolError
# import time

def has_tweet_been_replied_to(user_name, tweet_id):
    for reply in tweepy.Cursor(api.search, q = "to:" + user_name, since_id = tweet_id).items():
        print("Found reply by:@" + reply.user.screen_name + " to:@" + user_name)

        if reply.in_reply_to_status_id_str == tweet_id:
            if reply.user.screen_name == "NCTsongbot":
                return True

    return False

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

# splits the lines of the txt file with all the links of the songs
lines = open('songs.txt').read().splitlines()

latest_tweet_id = "1167466263960018944"

# searches for any tweet that includes '@NCTsongbot'
for tweet in tweepy.Cursor(api.search, q='@NCTsongbot', since_id=latest_tweet_id).items(1):
    print("Found tweet by:@" + tweet.user.screen_name)
    if has_tweet_been_replied_to(tweet.user.screen_name, tweet.id_str) == False:
        # api.update_status("@" + tweet.user.screen_name + " " + random.choice(lines), tweet.id)
        print("responded to @" + tweet.user.screen_name)


#END














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
