from bs4 import BeautifulSoup
from flask import Flask, render_template, request, redirect, url_for
from flask import jsonify
import json
import plot_data
import get_news
import db_op
from pymongo import MongoClient
import config
import get_sentiment
import pickle


# Flask App
app = Flask(__name__, static_url_path='/static')
def load_obj(name):
    with open('./obj/' + name + '.pkl', 'rb') as f:
        return pickle.load(f)
ner_dict = load_obj('tweet_10000')
ner_id = load_obj('tweet_id_10000')

d = dict(zip(range(0,len(ner_id.keys())),sorted(list(ner_id.keys()))))
print d
result = d

@app.route("/")
def home():
    return render_template("index.html", result=result)


@app.route('/graph/', methods=['GET', 'POST'])
def graph():
    # req = request.args.get('ner')
    # print req
    req = json.loads(request.form.to_dict().keys()[0])['ner'].encode('utf-8')
    print req

    # print request.args.get('ner')

    # print len(ner_id['trump'])
    time = db_op.get_time(map(int, ner_id[req]))
    print time
    # print len(time)
    plot_data.plot_time(time)
    log, lat = db_op.get_coord(map(int, ner_id[req]))
    # print log, lat
    plot_data.plot_loc(log, lat)
    headline = get_news.getNews([req])
    print headline
    h_s, t_s = get_sentiment.getSentiment(headline, {req: ner_dict[req]})

    plot_data.plotSentiment(h_s, t_s)

    
    return str(0)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5003)
