import json
from functools import reduce
import requests

dat = 'LNU04000000'

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

def run(start="2003", end="2022"):
    out = pull_data(dat, start, end)
    outt = dict([(x['year']+'-'+x['periodName'], x['value']) for x in out])
    return outt
