import numpy as np
import normalize
import combine
import json
import pca

def run(start, end):
    combine.run(start, end)
    normalize.run("Consumers_2003-2022.json")
    normalize.run("Industry_2003-2022.json")
    normalize.run("2003-2022.json")
    data = json.load(open("All_2003-2022.json"))
    open('axis.txt', 'w').close()
    people = pca.run("Normalized_2003-2022.json")
    consume = pca.run("Normalized_Consumers_2003-2022.json")
    produce = pca.run("Normalized_Industry_2003-2022.json")
    out = np.array([[0 for _ in range(len(people)+len(consume)+len(produce))]])
    for year in data:
        try:
            pending = [0 for _ in range(len(people) + len(consume) + len(produce))]
            pointer = 0
            datyear = data[year]
            for combs in people:
                for k in combs:
                    pending[pointer] += combs[k] * datyear[k]
                pointer += 1
            for combs in consume:
                for k in combs:
                    pending[pointer] += combs[k] * datyear[k]
                pointer += 1
            for combs in produce:
                for k in combs:
                    pending[pointer] += combs[k] * datyear[k]
                pointer += 1
            out = np.append([pending], out, axis=0)
        except Exception as e:
            print("Warning: Insufficient data in ", e)
            continue
    out = out[:-1]
    return out
