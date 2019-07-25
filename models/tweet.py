from tweet_types import Tweet_type

class Tweet(object):
    line = 0
    image = ""
    type = None

    # Constructor
    def __init__(self, type, args = None):
        if type == Tweet_type.final:
            message = get_message(type, args)
            image = get_image(type, args)
