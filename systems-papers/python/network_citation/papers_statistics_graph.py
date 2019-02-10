#######################################
# Variables of interest:
# - gA:
#     - outCitations
# - gB:
#     - inCitations
#     - year

# utilities
import sys
import os
import json
import numpy as np
import utils.shared_utils as utils
import utils.conf_utils as conf_utils
import utils.colors as u_colors
from tqdm import tqdm

# modules
import utils.data as u_data
import semantic_scholar.s2data as s2data

# matplotlib
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import colors
from matplotlib.ticker import PercentFormatter
np.random.seed(19680801)

################################################################
print("[#] Loading Data:")

statistics = json.load(open("../statistics/papers_statistics.json"))
gA_statistics = statistics["gA"]
gB_statistics = statistics["gB"]

################################################################
print("[#] Writing Results:")

fig = plt.figure(figsize=(13/1.4,6/1.4))
ax = fig.add_subplot(111)

if False:
    # gA : outCitations    
    data = np.array(gA_statistics["outCitations"])
    ax.hist(data , bins=120)
    
    plt.title("Distribution of outCitations in Group A")
    plt.xlabel("number of outCitations")
    plt.ylabel("frequency")
    plt.show()
    # TODO
    # ax.vlines(x, ymin, ymax, colors='k', linestyles='solid', label='', *, data=None, **kwargs)
    # x : scalar or 1D array_like
    # x-indexes where to plot the lines.
    # ymin, ymax : scalar or 1D array_like
    # Respective beginning and end of each line. If scalars are provided, all lines will have same length.
    # colors : array_like of colors, optional, default: 'k'
    # linestyles : ['solid' | 'dashed' | 'dashdot' | 'dotted'], optional
    # label : string, optional, default: ''

if False:
    # gB : inCitationsRate
    plt.yscale('log', nonposy='clip')
    
    data = np.array(gB_statistics["inCitationsRate"])
    ax.hist(data , bins=100)
    
    plt.title("Distribution of inCitations per Year in Group B")
    plt.xlabel("inCitations per year after 2018")
    plt.ylabel("frequency")
    plt.show()

if False:
    # gB : inCitations
    plt.yscale('log', nonposy='clip')

    data = np.array(gB_statistics["inCitations"])
    ax.hist(data , bins=100)

    plt.title("Distribution of inCitations in Group B")
    plt.xlabel("number of inCitations")
    plt.ylabel("frequency")
    plt.show()

if False:
    # gB : year
    data = np.array(gB_statistics["years"])
    ax.hist(data , bins=( max(data) - min(data) ))
    
    plt.title("Distribution of Publication Years in Group B")
    plt.xlabel("year published")
    plt.ylabel("frequency")
    plt.show()

if False:
    # gA : author_collaborations
    # plt.yscale('log', nonposy='clip')
    data = np.array(list(gA_statistics["author_collaborations"].values()))
    ax.hist(data , bins=( max(data) - min(data) ))

    # raw = np.array(list(gA_statistics["author_collaborations"].values()))

    # data = []
    # for i in range(max(raw)):
    #     total = len([ x for x in raw if i >= x ])
    #     data.append(total)
    # data = np.array(data)

    # ax.fill_between( np.arange(0,len(data)), 0, data )
    
    plt.title("Collaboration Counts of Authors")
    # plt.xlabel("number of co-authors per paper")
    plt.ylabel("frequency")
    plt.ylabel("authors with at least x collaborationis")
    plt.show()

if True:
    # gA : author_collaborations
    # plt.yscale('log', nonposy='clip')
    data = gA_statistics["paper_authors"]
    data = [ d for d in data if d > 0 ]
    data = np.array(data)

    # total = len(data)
    # xs = []
    # t  = 0
    # for i in range(100):
    #     x = len([d for d in data if d == i])/total
    #     if t + x > 0.5: break
    #     xs.append(x)
    #     t += x
    # print(t,xs)

    ax.hist(data , bins=( max(data) - min(data) ))

    # raw = gA_statistics["paper_authors"]
    # data = []
    # for i in range(max(raw)):
    #     total = len([ x for x in raw if i >= x ])
    #     data.append(total)
    # data = np.array(data)

    # [print(i,":",data[i]/total) for i in range(len(data))]

    # ax.fill_between( np.arange(0,len(data)), 0, data )
    
    plt.title("Papers' Author Counts")
    plt.xlabel("number of authors per paper")
    plt.ylabel("count")
    plt.show()

if False:
    # gA confs : indegrees
    raw = [34, 27, 30, 16, 123, 84, 117, 1, 37, 56, 86, 10, 16, 21, 4, 16, 1, 101, 115, 1, 89, 6, 14, 21, 32, 0, 11, 57, 61, 7, 49, 16, 40, 16, 32, 35, 2, 2, 12, 4, 14, 26, 6, 17, 6, 105, 6, 3, 5, 42, 23, 41, 1, 7, 0]
    
    data = []
    for i in range(max(raw)):
        total = len([ x for x in raw if i >= x ])
        data.append(total)
    data = np.array(data)

    ax.fill_between( np.arange(0,len(data)), 0, data )

    plt.title("In-citation Distribution among Conferences")
    plt.xlabel("number of in-citations")
    plt.ylabel("conferences with at least x in-citations")
    plt.show()