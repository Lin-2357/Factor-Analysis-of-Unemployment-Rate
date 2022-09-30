import json
import math
import numpy


def run(file):
    data = json.load(open(file))
    out = {}
    for factor in data:
        out[factor] = {}
        listdat = []
        for year in data[factor]:
            if data[factor][year] != "NaN" and not math.isnan(data[factor][year]):
                listdat.append(data[factor][year])
        mean = numpy.mean(listdat)
        std = numpy.std(listdat)
        for year in data[factor]:
            if data[factor][year] != "NaN" and not math.isnan(data[factor][year]):
                out[factor][year] = (data[factor][year] - mean) / std
            else:
                out[factor][year] = data[factor][year]
    with open("Normalized_"+file, "w") as outfile:
        json.dump(out, outfile)
