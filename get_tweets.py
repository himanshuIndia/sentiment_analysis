import config
from twython import Twython, TwythonStreamer
import json
from pymongo import MongoClient
import sys

client = MongoClient()
db = client[config.db_name]
count = 0
class MyStreamer(TwythonStreamer):
    def on_success(self, data):
        global count
        if 'text' in data:
            #             with open('data.txt', 'w') as outfile:
            #                 json.dump(data, outfile)
            print (data['text'])
            posts = db.posts
            posts.insert_one(data).inserted_id
            count += 1
        if count > config.MAX_TWEETS:
            self.disconnect()

    def on_error(self, status_code, data):
        print(status_code)

        # Want to stop trying to get data because of the error?
        # Uncomment the next line!
        self.disconnect()

def getTweets(twitter_key,twitter_secret,app_token,app_secret):
    stream = MyStreamer(twitter_key,twitter_secret,app_token,app_secret)
    stream.statuses.filter(locations=config.location_US, language='en')
