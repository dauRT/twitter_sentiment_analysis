import re
from textblob import TextBlob


class Tweet(object):
    def __init__(self, text):
        self.text = text
        self.polarity = self.get_tweet_sentiment()

    def clean_tweet(self):
        self.text = ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", self.text).split())

    def get_tweet_sentiment(self):
        self.clean_tweet()
        return TextBlob(self.text).sentiment.polarity
