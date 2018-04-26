import config
import get_ner
import get_tweets
import get_news
import get_sentiment
import plot_data
from pymongo import MongoClient

client = MongoClient()
db = client[config.db_name]
posts = db.posts


get_tweets.getTweets(config.twitter_key,config.twitter_secret, config.app_token,config.app_secret)

keys,ner_dict = get_ner.getNER(posts,config.top_n)

headlines = get_news.getNews(keys)

h_s, t_s = get_sentiment.getSentiment(headlines,ner_dict)

plot_data.plotSentiment(h_s,t_s)