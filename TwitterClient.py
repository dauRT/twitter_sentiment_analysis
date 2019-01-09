import tweepy
from tweepy import OAuthHandler


class TwitterClient(object):
    def __init__(self):
        api_key = 'your-key-goes-here'
        api_secret_key = 'you-secret-key-goes-here'
        access_token = 'your-access-token-goes-here'
        secret_access_token = 'your-secret-access-token-goes-here'

        try:
            self.auth = OAuthHandler(api_key, api_secret_key)
            self.auth.set_access_token(access_token, secret_access_token)
            self.api = tweepy.API(self.auth)
            print('authenticated successfully')
        except:
            print('Could not authenticate')

    def get_tweets(self, query, count=15):
        try:
            return self.api.search(q=query, count=count)
        except:
            print('Error in reading the tweet')

