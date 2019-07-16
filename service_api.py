import twitter
import datetime
from data_secrets import *
from data_constants import *

api = twitter.Api(consumer_key=consumer_key,
                  consumer_secret=consumer_secret,
                  access_token_key=access_token,
                  access_token_secret=access_token_secret)

last_tweet_id = None

def tweet(message):
    global last_tweet_id
    tweet = api.PostUpdate(status = message, in_reply_to_status_id=last_tweet_id)
    last_tweet_id = tweet.id_str

def print_or_tweet(message):
    if live:
        tweet(message.decode("utf8"))
    else:
        print(message)

def startListeningMDs():
    while not finished:
        answerDMs()
        time.sleep(listeningDelay)

# def check_dms():
#     global max_id
#     temporal_max_id = max_id
#     min_id = None
#     stop = False
#
#     while stop == False:
#         print "get 3 mds since " + str(max_id) + " until " + str(min_id)
#         direct_messages = api.GetDirectMessages(return_json=True, count=3, since_id=max_id, max_id=min_id)['events']
#         if len(direct_messages) == 0:
#             stop = True
#         for dm in list(reversed(direct_messages)):
#              id = dm['id']
#              created_timestamp = dm['created_timestamp']
#              text = dm['message_create']['message_data']['text']
#              sender_id = dm['message_create']['sender_id']
#              recipient_id = dm['message_create']['target']['recipient_id']
#              type = dm['type']
#
#              if min_id == None:
#                  min_id = str(int(id) - 1)
#              if temporal_max_id == None:
#                  temporal_max_id = id
#
#              if id < min_id:
#                  min_id = str(int(id) - 1)
#              if id > temporal_max_id:
#                  temporal_max_id = id
#              print "md: " + text + ", id: " + id
#     max_id = temporal_max_id
