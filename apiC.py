import json
from functools import reduce
import requests
import pandas

dat = [['U.S. city average Purchasing power of the consumer dollar Not Seasonally Adjusted       ', 'CUUR0000SA0R'], ['U.S. city average Apparel Not Seasonally Adjusted       ', 'CUUR0000SAA'], ['U.S. city average Education and communication Not Seasonally Adjusted       ', 'CUUR0000SAE'], ['U.S. city average Food and beverages Not Seasonally Adjusted       ', 'CUUR0000SAF'], ['U.S. city average Other goods and services Not Seasonally Adjusted       ', 'CUUR0000SAG'], ['U.S. city average Housing Not Seasonally Adjusted       ', 'CUUR0000SAH'], ['U.S. city average Medical care Not Seasonally Adjusted       ', 'CUUR0000SAM'], ['U.S. city average Recreation Not Seasonally Adjusted       ', 'CUUR0000SAR'], ['U.S. city average Transportation Not Seasonally Adjusted       ', 'CUUR0000SAT']]

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
    id = rows[1]
    data = pull_data(id, start, end)
    print(rows, "pulled from API call")
    for n in data:
        if 'year' in n and 'value' in n and 'periodName' in n:
            try:
                years[n['year']+"-"+n['periodName']] = float(n['value'])
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
        name = rows[0]
        item = retrieve(rows, start, end)
        out[name] = item
        print(item)
        print(name)

    with open("Consumers_"+start+"-"+end+".json", "w") as outfile:
        json.dump(out, outfile)
