#%matplotlib nbagg
import numpy as np
import matplotlib.pyplot as plt


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
    rects1 = ax.bar(ind, news, width, color='r')

    tweet = [t_s[x] for x in t_s.keys()]

    rects2 = ax.bar(ind + width, tweet, width, color='y')

    # add some text for labels, title and axes ticks
    ax.set_ylabel('Scores')
    ax.set_title('Sentiment')
    ax.set_xticks(ind + width / 2)
    ax.set_xticklabels(h_s.keys(), rotation=90)

    ax.legend((rects1[0], rects2[0]), ('news', 'tweet'))

    autolabel(ax,rects1)
    autolabel(ax,rects2)
    plt.savefig('fig.png')
    plt.show()