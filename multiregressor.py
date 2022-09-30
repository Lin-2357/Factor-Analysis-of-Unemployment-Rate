import json
import math
from scipy import stats

def run(file):

    data = json.load(open(file))

    def regress(x, y):
        rowx = [float(data[x][i]) for i in data[x]]
        rowy = [float(data[y][i]) for i in data[y]]
        newrx = []
        newry = []
        for i in range(len(rowx)):
            if rowx[i] != "NaN" and rowy[i] != "NaN":
                newrx.append(rowx[i])
                newry.append(rowy[i])
        rowx = newrx
        rowy = newry
        if len(rowx) * len(rowy) == 0:
            return None
        else:
            return stats.linregress(rowx, rowy).rvalue

    regressions = {}
    for x in data.keys():
        for y in data.keys():
            if x != y and y + " vs " + x not in regressions:
                regressions[x + " vs " + y] = regress(x, y)

    regressionlist = [(i, regressions[i]) for i in regressions.keys() if not math.isnan(regressions[i])]
    regressionlist.sort(key=lambda x:x[1])
    return regressionlist
