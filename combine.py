import json

def run(start="2003", end="2022"):
    total = {}
    total2 = {}

    dicts = [json.load(open("Normalized_"+start+"-"+end+".json")), json.load(open("Normalized_Industry_"+start+"-"+end+".json")),
             json.load(open("Normalized_Consumers_"+start+"-"+end+".json"))]

    for dictionary in dicts:
        for factor in dictionary.keys():
            for year in dictionary[factor]:
                if year not in total:
                    total[year] = {}
                if factor not in total2:
                    total2[factor] = {}
                total[year][factor] = dictionary[factor][year]
                total2[factor][year] = dictionary[factor][year]

    with open("All_" + start + "-" + end + ".json", "w") as outfile:
        json.dump(total, outfile)
    with open("AllFactor_" + start + "-" + end + ".json", "w") as outfile:
        json.dump(total2, outfile)
