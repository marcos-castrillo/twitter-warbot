import twitter
import datetime

from data.secrets import *
from data.constants import *

last_tweet_id = None

def tweet_line_from_file(filename, line_number):
    with open(filename, 'r') as file:
        for i, line in enumerate(file):
            if int(i) == int(line_number):
                print(line)
                return
                # tweet(line)

def tweet(message):
    global last_tweet_id, consumer_key, consumer_secret, access_token, access_token_secret

    api = twitter.Api(consumer_key=consumer_key,
                      consumer_secret=consumer_secret,
                      access_token_key=access_token,
                      access_token_secret=access_token_secret)

    tweet = api.PostUpdate(status = message.decode("utf8"), in_reply_to_status_id=last_tweet_id)
    last_tweet_id = tweet.id_str
