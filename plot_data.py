#%matplotlib nbagg
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import numpy as np
import pandas



def autolabel(ax,rects):
    """
    Attach a text label above each bar displaying its height
    """
    for rect in rects:
        height = rect.get_height()
        ax.text(rect.get_x() + rect.get_width() / 2.0, 1.05 * height,
                '%f' % float(height),
                ha='center', va='bottom', rotation=90)

def plotSentiment(h_s,t_s):
    N = len(h_s.keys())
    news = [h_s[x] for x in h_s.keys()]


    ind = np.arange(N)  # the x locations for the groups
    width = 0.35       # the width of the bars

    fig, ax = plt.subplots(figsize=(10,8))
    rects1 = ax.bar(ind, news, width, color='skyblue')

    tweet = [t_s[x] for x in t_s.keys()]

    rects2 = ax.bar(ind + width, tweet, width, color='coral')

    # add some text for labels, title and axes ticks
    ax.set_ylabel('Scores')
    ax.set_title('Sentiment')
    ax.set_xticks(ind + width / 2)
    ax.set_xticklabels(h_s.keys(), rotation=90)

    ax.legend((rects1[0], rects2[0]), ('news', 'tweet'))

    autolabel(ax,rects1)
    autolabel(ax,rects2)
    plt.savefig('./static/images/graph/gp3.png')
    fig.clf()
    plt.clf()
    #plt.show()


def plot_loc(loc_log,loc_lat):
    plt.figure(figsize=(100, 50))
    map = Basemap(projection='merc',
                  resolution='h', area_thresh=0.1,
                  llcrnrlon=-124.9, llcrnrlat=23.81,
                  urcrnrlon=-57.58, urcrnrlat=57.37)

    map.drawcoastlines()
    map.drawcountries(color='green')
    map.fillcontinents(color='skyblue')
    map.drawmapboundary()
    map.drawstates(color='blue')

    lons = list(loc_log.values())
    lats = list(loc_lat.values())
    x, y = map(lons, lats)
    map.plot(x, y, 'ro', markersize=50)

    # lon = -135.3318
    # lat = 57.0799
    # x,y = map(lon, lat)
    # map.plot(x, y, 'bo', markersize=1, )
    plt.savefig('./static/images/graph/gp1.png', bbox_inches='tight', pad_inches=0.1)
    #plt.show()
    plt.clf()


def plot_time(time):
    ones = [1] * len(time)
    idx = pandas.DatetimeIndex(time)
    ITAvWAL = pandas.Series(ones, index=idx)

    # Resampling
    per_minute = ITAvWAL.resample('2S', how='sum').fillna(0)
    plt.plot(per_minute.keys(), per_minute.values)
    #plt.xticks(rotation=90)
    plt.savefig('./static/images/graph/gp2.png')
    #plt.show()
    plt.clf()