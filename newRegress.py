import math

import numpy as np

import newAxis
import numpy
import matplotlib.pyplot as plt
from scipy import stats

def run(start, end):
    newdat = newAxis.run(start, end).T
    newr = []
    print("start regression...")
    for i in range(len(newdat)):
        for j in range(i + 1, len(newdat)):
            reg = stats.linregress(newdat[i], newdat[j])
            newr.append(((i, j), reg.rvalue, reg.slope, reg.intercept))

    newr.sort(key=lambda x: -math.fabs(x[1]))
    print("start plotting...")
    i = 0
    for rows in newr:
        plt.scatter(newdat[rows[0][0]], newdat[rows[0][1]])
        minx = min(newdat[rows[0][0]])
        maxx = max(newdat[rows[0][0]])
        xs = numpy.array([minx, maxx])
        plt.plot(xs, xs * rows[2] + np.array([rows[3], rows[3]]))
        plt.savefig("./plots/" + str(i) + "-" + str(rows[0]) + ".jpg")
        plt.clf()
        i += 1

    with open("newAxisRegress.txt", "w") as file:
        for row in newr:
            file.write(str(row))
            file.write("\n\n")