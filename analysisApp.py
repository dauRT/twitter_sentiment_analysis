from TwitterClient import TwitterClient
from tweet import Tweet
import os
import logging


filename = ''.join([os.getcwd(), '\\analysis_app.log'])
logging.basicConfig(filename=filename, level=logging.INFO)


def main():
    api = TwitterClient()
    positive, negative, neutral = 0, 0, 0
    count = 100
    for tweet in api.get_tweets(query='Python', count=count):
        tw = Tweet(tweet.text)
        logging.info('Tweet text:: ' + tw.text)

        if tw.polarity > 0:
            positive += 1
            logging.info('Positive tweet, polarity::{}'.format(tw.polarity))
        elif tw.polarity == 0:
            neutral += 1
            logging.info('Neutral tweet, polarity::{}'.format(tw.polarity))
        else:
            negative += 1
            logging.info('Negative tweet, polarity::{}'.format(tw.polarity))

    logging.info("Positive tweets percentage:: {} %".format(100 * positive/count))
    logging.info("Neutral tweets percentage:: {} %".format(100 * neutral / count))
    logging.info("Negative tweets percentage:: {} %".format(100 * negative/count))


if __name__ == "__main__":
    main()
