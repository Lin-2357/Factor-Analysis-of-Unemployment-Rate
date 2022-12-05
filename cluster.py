import json
import numpy as np
import newAxis
import numpy
from sklearn.cluster import KMeans

def sqdist(x, y):
    diff = np.subtract(x, y)
    out = np.sum(np.multiply(diff, diff))
    return out

def variance(dat, lbs, clusters):
    clus = [[] for _ in range(clusters)]
    for i in range(len(lbs)):
        clus[lbs[i]].append(dat[i])
    return [(numpy.nanvar(x), len(x)) for x in clus]
def mean(dat, lbs, clusters):
    clus = [[] for _ in range(clusters)]
    for i in range(len(lbs)):
        clus[lbs[i]].append(dat[i])

    return [numpy.median(x) for x in clus]

def rate(dat, lbs, clusters,m):
    clus = [[] for _ in range(clusters)]
    for i in range(len(lbs)):
        clus[lbs[i]].append(dat[i])
    return [len([i for i in x if i > m])/len(x) for x in clus]

def run(start, end):
    dat = newAxis.run(start, end).T
    with open("axis.txt") as f:
        axislines = f.readlines()
    unemploymentlength = (len("".join(axislines)[:"".join(axislines).index("\n\n\n\n\n")].split("\n")) + 1) // 2 + 1
    dat1 = numpy.array(dat[unemploymentlength:]).T
    dat2 = numpy.array(dat[:unemploymentlength]).T
    for k in range(1, 7):
        print("**********")
        print("Clustering with", k, "clusters:")
        km = KMeans(n_clusters=k, random_state=0).fit(dat1)
        print("Average Inertia", km.inertia_ / len(dat1))
        ct = km.cluster_centers_
        n = len(ct) * (len(ct) - 1) // 2
        meandistance = 0
        for i in range(len(ct)):
            for j in range(i + 1, len(ct)):
                meandistance += sqdist(ct[i], ct[j]) / n
        print("Average distance between centroids", meandistance)
        print("Overall Variance in Unemployment Rate", numpy.nanvar(dat2.T[0].T))
        print("Overall median in Unemployment Rate", numpy.nanmedian(dat2.T[0].T))
        print("Variance in Unemployment in each cluster", variance(dat2.T[0].T, km.labels_, k))
        print("Median in Unemployment in each cluster", mean(dat2.T[0].T, km.labels_, k))
        print("Rate of > 5% in Unemployment in each cluster", rate(dat2.T[0].T, km.labels_, k, 5))
        dicout = {lb:[] for lb in range(k)}
        for index in range(len(km.labels_)):
            dicout[km.labels_[index]].append((tuple(dat.T[index])))
        with open("./kmeans/"+str(k)+".json", 'w') as fk:
            json.dump(dicout, fk)

run('2003','2022')

