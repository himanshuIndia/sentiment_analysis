import json
import re
from nltk.tag import StanfordNERTagger
from nltk.tokenize import word_tokenize
import config
from twython import Twython, TwythonStreamer
from pymongo import MongoClient
import sys
import operator
import ast


client = MongoClient()
db = client[config.db_name]
posts = db.posts
st = StanfordNERTagger('/home/bravo/stanford_nltk_models/stanford-ner-2018-02-27/classifiers/english.all.3class.distsim.crf.ser.gz','/home/bravo/stanford_nltk_models/stanford-ner-2018-02-27/stanford-ner.jar',encoding='utf-8')

def clean_tweet(tweet):
    return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", tweet).split())


def getNER(posts,num_keys):
    tweet = []
    tweet_id = []
    for post in posts.find():
        tweet.append(clean_tweet(post['text']).encode('utf-8'))
        tweet_id.append(post['id'])

    count = 0
    ner_dict = {}
    ner_id = {}
    ner_count = {}
    for i,id in zip(tweet,tweet_id):
        count += 1
        #print (count)
        tokenized_text = word_tokenize(i)
        classified_text = st.tag(tokenized_text)
        for j in classified_text:
            # if (j not in person) and (j not in organization) and (j not in location) and (j not in misc):
            if (j[1] == 'PERSON') or (j[1] == 'LOCATION') or (j[1] == 'ORGANIZATION') or (j[1] == 'MISC'):
                if j[0].lower().encode('utf-8') in ner_dict.keys():
                    ner_dict[j[0].lower().encode('utf-8')].append(i)
                    ner_id[j[0].lower().encode('utf-8')].append(id)
                    ner_count[j[0].lower().encode('utf-8')] += 1
                else:
                    ner_dict[j[0].lower().encode('utf-8')] = [i]
                    ner_id[j[0].lower().encode('utf-8')] = [id]
                    ner_count[j[0].lower().encode('utf-8')] = 1

    print (ner_count, ner_dict)

    #count = 0
    key_max = []
    for i in range(0,num_keys):
        #print(ner_count)
        key_max.append(max(ner_count.items(), key=operator.itemgetter(1))[0])
        ner_count.pop(max(ner_count.items(), key=operator.itemgetter(1))[0])

    key_max = [key.encode('utf-8') for key in key_max]

    return key_max,ner_dict,ner_count