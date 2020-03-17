import twitter
import datetime

from data.secrets import *
from data.constants import *

def tweet_line_from_file(file_path, line_number, image_path = None, image_2_path = None, last_tweet_id = None):
    with open(image_path, 'rb') as image:
        with open(file_path, 'r') as file:
            for i, line in enumerate(file):
                if int(i) == int(line_number):
                    print(line)
                    return tweet(line, image_path, image_2_path, last_tweet_id)

def tweet(message, image_path, image_2_path = None, last_tweet_id = None):
    global consumer_key, consumer_secret, access_token, access_token_secret

    api = twitter.Api(consumer_key=consumer_key,
                      consumer_secret=consumer_secret,
                      access_token_key=access_token,
                      access_token_secret=access_token_secret)

    image_list = [image_path]
    if image_2_path != None and os.path.exists(image_2_path):
        image_list.append(image_2_path)

    tweet = api.PostUpdate(status = message.decode("utf8"), in_reply_to_status_id=last_tweet_id, media=image_list)
    return tweet.id_str
