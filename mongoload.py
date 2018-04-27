from pymongo import MongoClient
client = MongoClient()
db = client['twitter']
with open('./obj/twitter_hashtags.txt') as f:
    lines = f.read().splitlines()

import json
import ast

count = 0
tweet = []
# ast.literal_eval() return a dict object, we must use json.dumps to get JSON string
for i in lines:
    a = ast.literal_eval(i)
    a = json.dumps(a.encode('utf-8').strip)
    a = json.loads(a)
    posts = db.posts
    posts.insert_one(a).inserted_id

    count += 1