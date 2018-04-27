from pymongo import MongoClient
import config


client = MongoClient()
db = client[config.db_name]
posts = db.posts

def get_coord(t_id):
    loc_log = {}
    loc_lat = {}
    for id in t_id:
        count2 = 0
        for post in posts.find({'id':id}):
            log = 0.0
            lat = 0.0
            count = 0.0
            # pprint.pprint(post)
            # print(post['id'])
            if post['place'] and (post['id'] not in loc_log.keys()):
                for i in post['place']['bounding_box']['coordinates'][0]:
                    log += i[0]
                    lat += i[1]
                    count += 1
                log = log / count
                lat = lat / count
                loc_log[post['id']] = log
                loc_lat[post['id']] = lat
    return loc_log, loc_lat

def get_time(t_id):
    time = []
    for i in t_id:
        count2 = 0
        for post in posts.find({'id': i}):
            time.append(post['created_at'])

    return time