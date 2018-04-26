from textblob import TextBlob


def get_tweet_sentiment(sent):
    analysis = TextBlob(sent)
    return analysis.sentiment.polarity

def getSentiment(headlines,ner_dict):
    headline_score = {}
    tweet_score = {}
    for i in headlines.keys():
        headline_score[i] = 0.0
        tweet_score[i] = 0.0
        for j in headlines[i]['articles']:
            headline_score[i] += float(get_tweet_sentiment(j['title']))
        headline_score[i] = headline_score[i] / headlines[i]['totalResults']
        for k in ner_dict[i]:
            tweet_score[i] += float(get_tweet_sentiment(k))
        tweet_score[i] = tweet_score[i] / float(len(ner_dict[i]))


    return headline_score, tweet_score

