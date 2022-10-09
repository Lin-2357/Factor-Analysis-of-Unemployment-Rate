import json
import math
import numpy
from sklearn import linear_model
import normalize

with open('newAxisRegress.txt') as f:
    lines = f.readlines()

with open("axis.txt") as f:
    axislines = f.readlines()

def weight(source, axis, keys):
    outdic = {k:"NaN" for k in keys}
    for k in outdic:
        tmp = 0
        try:
            for x in axis:
                tmp += source[x][k] * axis[x]
            outdic[k] = tmp
        except Exception:
            continue
    return outdic

def mtregress(start, end, maxnum, cleanedline, cleanaxis, keys):
    cleanedaxis = [{x.split("', ")[0][1:]: float(x.split("', ")[1]) for x in y[:maxnum]} for y in cleanaxis]

    normalize.run("AllFactor_" + start + "-" + end + ".json")
    with open("Normalized_AllFactor_" + start + "-" + end + ".json") as fac:
        duc = json.load(fac)

    for pairs in cleanedline:
        yk = cleanedaxis[pairs[0]]
        xk = cleanedaxis[pairs[1]]
        dicy = weight(duc, yk, keys)
        dicx = [weight(duc, {x:1}, keys) for x in xk]
        y = []
        x = []
        for i in keys:
            if dicy[i] != "NaN" and all([dicxx[i] != "NaN" for dicxx in dicx]):
                y.append(dicy[i])
                x.append(numpy.array([dicxx[i] for dicxx in dicx]))
        regr = linear_model.LinearRegression()
        x0 = numpy.array(x)
        y0 = numpy.array(y)
        regr.fit(x0, y0)
        print("multiregression for", maxnum, "attributes in pair", pairs)
        sc = regr.score(x0, y0)
        print("r^2 value is:", sc)
        with open("./mtregress/"+str(pairs)+".txt", 'a') as wr:
            wr.writelines(["MultiRegression for "+str(maxnum)+" Attributes:", "\n", "Attributes: " + \
                           str(xk), "\n", "R^2: " + str(sc), "\n", "Coefficients: " + str(list(regr.coef_)), "\n" \
                              , "Intercept: "+ str(regr.intercept_), "\n"])

def run(start, end, maxattr=8, minr = 0.5):
    unemploymentlength = (len("".join(axislines)[:"".join(axislines).index("\n\n\n\n\n")].split("\n")) + 1) // 2
    keys = []
    [keys.extend(x) for x in [[str(year) + "-" + month for month in
                ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October",
                 "November", "December"] for year in range(int(start), int(end) + 1)]]]

    cleanline = [x[1:-3].split(', ') for x in lines if x != '\n']
    cleanaxis = [x[2:-3].split('), (') for x in axislines if x != '\n']
    cleaningline = [(int(x[0][1:]), int(x[1][:-1])) for x in cleanline if math.fabs(float(x[2])) > minr]
    cleanedline = [x for x in cleaningline if x[0] < unemploymentlength and x[1] >= unemploymentlength]
    for pairs in cleanedline:
        with open("./mtregress/" + str(pairs) + ".txt", 'w') as g:
            g.write("")
    for i in range(1, maxattr + 1):
        mtregress(start, end, i, cleanedline, cleanaxis, keys)

run('2003', '2022')