import json
from functools import reduce
import requests

dat = [['Men', 'White', '25', 'Monthly', 'LNU04000230'], ['Men', 'White', '35', 'Monthly', 'LNU04000237'], ['Men', 'White', '45', 'Monthly', 'LNU04000244'], ['Women', 'White', '25', 'Monthly', 'LNU04000385'], ['Women', 'White', '35', 'Monthly', 'LNU04000392'], ['Women', 'White', '45', 'Monthly', 'LNU04000399'], ['Men', 'Black', '25', 'Monthly', 'LNU04015832'], ['Men', 'Black', '35', 'Monthly', 'LNU04015839'], ['Men', 'Black', '45', 'Monthly', 'LNU04015845'], ['Women', 'Black', '25', 'Monthly', 'LNU04000457'], ['Women', 'Black', '35', 'Monthly', 'LNU04000459'], ['Women', 'Black', '45', 'Monthly', 'LNU04000461'], ['Men', 'Asian', '25', 'Monthly', 'LNU04034989'], ['Men', 'Asian', '35', 'Monthly', 'LNU04034990'], ['Men', 'Asian', '45', 'Monthly', 'LNU04034991'], ['Women', 'Asian', '25', 'Monthly', 'LNU04034996'], ['Women', 'Asian', '35', 'Monthly', 'LNU04034997'], ['Women', 'Asian', '45', 'Monthly', 'LNU04034998']]

def pull_data(series_id, start, end):
    # Specify json as content type to return
    headers = {'Content-type': 'application/json'}

    # Submit the list of series as data
    data = json.dumps({"seriesid": [series_id], "startyear": start, "endyear": end,
                       "registrationkey": "4599fa048f824abc950fa9928d6da426"})

    # Post request for the data
    p = requests.post('https://api.bls.gov/publicAPI/v2/timeseries/data/', data=data, headers=headers)
    # change p into json type for further querying
    json_data = json.loads(p.text)

    # query data
    results = json_data
    return results['Results']['series'][0]['data']

"""
a = pandas.Series([1], index=[2])
b = pandas.Series([3], index=[0])
c = pandas.concat([a,b], ignore_index=False, axis=0)
print(c)
"""

def retrieve(rows, start, end):
    years = {}
    id = rows[4]
    data = pull_data(id, start, end)
    print(rows, "pulled from API call")
    for n in data:
        if 'year' in n and 'value' in n and 'periodName' in n:
            try:
                years[n['year'] + "-" + n['periodName']] = float(n['value'])
            except Exception:
                pass
        else:
            print("error in data:", rows)
            return
    print(rows, "deployed in dataset")
    return years

def run(start="2003", end="2022"):
    out = {}
    for rows in dat:
        name = reduce(lambda x, y: x + " " + y, rows[:4])
        item = retrieve(rows, start, end)
        out[name] = item
        print(item)
        print(name)

    with open(start+"-"+end+".json", "w") as outfile:
        json.dump(out, outfile)
