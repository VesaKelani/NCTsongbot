import tweepy # version 3.8.0
from credentials import *
import random
from requests.exceptions import Timeout, ConnectionError
from requests.packages.urllib3.exceptions import ReadTimeoutError, ProtocolError
import time

BOT_USER_NAME = "NCTsongbot"
ONE_MIN = 60
FIFTEEN_MIN = 60 * 15

def has_tweet_been_replied_to(user_name, tweet_id):
    for reply in tweepy.Cursor(api.search,
                                q = "@" + user_name,
                                since_id = tweet_id).items():
        print("Found reply by:@" + reply.user.screen_name + " to:@" + user_name)
        if reply.in_reply_to_status_id_str == tweet_id:
            if reply.user.screen_name == BOT_USER_NAME:
                return True
    return False

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
api = tweepy.API(auth)

try:
    api.verify_credentials()
    print("Authentication OK")
except BaseException as e:
    print(e.reason)


songs = open('songs.txt').read().splitlines()

while True:
    latest_tweet_id = open('latest_tweet_id.txt').read()

    try:
        print('Checking for tweets..')

        is_latest_tweet = True
        for tweet in tweepy.Cursor(api.search,
                                    q="@" + BOT_USER_NAME,
                                    since_id=latest_tweet_id).items():
            print("Found tweet by @" + tweet.user.screen_name)
            api.update_status(
                    "@" + tweet.user.screen_name + " " + random.choice(songs),
                    tweet.id_str)
            print("Responded to @" + tweet.user.screen_name)

            if is_latest_tweet:
                with open('latest_tweet_id.txt', 'w') as latest_tweet_id_file:
                    latest_tweet_id_file.write(tweet.id_str)

            is_latest_tweet = False
    except (
        tweepy.TweepError,
        tweepy.RateLimitError,
        Timeout,
        ConnectionError,
        ReadTimeoutError,
        ProtocolError
            ) as e:
        print(e.reason)
        time.sleep(FIFTEEN_MIN)

    time.sleep(ONE_MIN) # to abide by rate limit
