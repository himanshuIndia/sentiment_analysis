from newsapi import NewsApiClient

def getNews(keys):
    newsapi = NewsApiClient(api_key='3f96913828dc480b8d85cdbad8013a53')
    top_headlines = {}
    # /v2/top-headlines
    for i in keys:
        print (i)
        top_headlines[i] = newsapi.get_top_headlines(q=i,language='en')

    headlines = {}
    count = 0
    for i in keys:
        if top_headlines[i]['totalResults'] != 0:
            headlines[i] = top_headlines[i]
            count += 1

    return headlines