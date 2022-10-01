import json
from functools import reduce
import requests
import pandas

#dat = [['Logging Logging', 'PCU1133--1133--'], ['Oil and gas extraction Oil and gas extraction', 'PCU211---211---'], ['Crude petroleum and natural gas extraction Crude petroleum and natural gas extraction', 'PCU211111211111'], ['Natural gas liquids extraction Natural gas liquids extraction', 'PCU211112211112'], ['Coal mining Coal mining', 'PCU2121--2121--'], ['Metal ore mining Metal ore mining', 'PCU2122--2122--'], ['Nonmetallic mineral mining & quarrying Nonmetallic mineral mining & quarrying', 'PCU2123--2123--'], ['Mining support activities Mining support activities', 'PCU213---213---'], ['Electric power transmission, control, and distribution Electric power transmission, control, and distribution', 'PCU22112-22112-'], ['Food mfg Food mfg', 'PCU311---311---'], ['Wood product manufacturing Wood product manufacturing', 'PCU321---321---'], ['Textile mills Textile mills', 'PCU313---313---'], ['Apparel manufacturing Apparel manufacturing', 'PCU315---315---'], ['Leather and allied product manufacturing Leather and allied product manufacturing', 'PCU316---316---'], ['Paper manufacturing Paper manufacturing', 'PCU322---322---'], ['Printing and related support activities Printing and related support activities', 'PCU323---323---'], ['Chemical mfg Chemical mfg', 'PCU325---325---'], ['Plastics and rubber products mfg Plastics and rubber products mfg', 'PCU326---326---'], ['Nonmetallic mineral product manufacturing Nonmetallic mineral product manufacturing', 'PCU327---327---'], ['Primary metal mfg Primary metal mfg', 'PCU331---331---'], ['Fabricated metal product mfg Fabricated metal product mfg', 'PCU332---332---'], ['Machinery manufacturing Machinery manufacturing', 'PCU333---333---'], ['Computer & electronic product mfg Computer & electronic product mfg', 'PCU334---334---'], ['Electrical equipment  and appliance mfg Electrical equipment  and appliance mfg', 'PCU335---335---'], ['Transportation equipment manufacturing Transportation equipment manufacturing', 'PCU336---336---'], ['Furniture & related product mfg Furniture & related product mfg', 'PCU337---337---'], ['Miscellaneous mfg Miscellaneous mfg', 'PCU339---339---'], ['Merchant wholesalers, durable goods Merchant wholesalers, durable goods', 'PCU423---423---'], ['Motor vehicle and parts dealers Motor vehicle and parts dealers', 'PCU441---441---'], ['Food and beverage stores Food and beverage stores', 'PCU445---445---'], ['Gasoline stations Gasoline stations', 'PCU447---447---'], ['Health and personal care stores Health and personal care stores', 'PCU446---446---'], ['Clothing and clothing accessories stores Clothing and clothing accessories stores', 'PCU448---448---'], ['Sporting goods, hobby, and book stores Sporting goods, hobby, and book stores', 'PCU451---451---'], ['General merchandise stores General merchandise stores', 'PCU452---452---'], ['Nonstore retailers Nonstore retailers', 'PCU454---454---'], ['Fuel dealers Fuel dealers', 'PCU45431-45431-'], ['Air transportation Air transportation', 'PCU481---481---'], ['Rail transportation Rail transportation', 'PCU482---482---'], ['Truck transportation Truck transportation', 'PCU484---484---'], ['Transportation support activities Transportation support activities', 'PCU488---488---'], ['U.S. Postal Service U.S. Postal Service', 'PCU491---491---'], ['Couriers and messengers Couriers and messengers', 'PCU492---492---'], ['Warehousing and storage Warehousing and storage', 'PCU493---493---'], ['Publishing industries, except Internet Publishing industries, except Internet', 'PCU511---511---'], ['Broadcasting, except Internet Broadcasting, except Internet', 'PCU515---515---'], ['Telecommunications Telecommunications', 'PCU517---517---'], ['Security, commodity contracts and like activity Security, commodity contracts and like activity', 'PCU523---523---'], ['Insurance carriers and related activities Insurance carriers and related activities', 'PCU524---524---'], ['Legal services Legal services', 'PCU5411--5411--'], ['Architectural, engineering and related services Architectural, engineering and related services', 'PCU5413--5413--'], ['Management and technical consulting services Management and technical consulting services', 'PCU5416--5416--'], ['Travel agencies Travel agencies', 'PCU56151-56151-'], ['Medical and diagnostic laboratories Medical and diagnostic laboratories', 'PCU6215--6215--'], ['Hospitals Hospitals', 'PCU622---622---'], ['Accommodation Accommodation', 'PCU721---721---']]
dat = [['Logging Logging', 'PCU1133--1133--'], ['Oil and gas extraction Oil and gas extraction', 'PCU211---211---'], ['Mining (except oil & gas) Mining (except oil & gas)', 'PCU212---212---'], ['Mining support activities Mining support activities', 'PCU213---213---'], ['Utilities Utilities', 'PCU221---221---'], ['Food mfg Food mfg', 'PCU311---311---'], ['Textile product mills Textile product mills', 'PCU314---314---'], ['Textile mills Textile mills', 'PCU313---313---'], ['Beverage & tobacco mfg Beverage & tobacco mfg', 'PCU312---312---'], ['Apparel manufacturing Apparel manufacturing', 'PCU315---315---'], ['Leather and allied product manufacturing Leather and allied product manufacturing', 'PCU316---316---'], ['Wood product manufacturing Wood product manufacturing', 'PCU321---321---'], ['Paper manufacturing Paper manufacturing', 'PCU322---322---'], ['Printing and related support activities Printing and related support activities', 'PCU323---323---'], ['Petroleum and coal products manufacturing Petroleum and coal products manufacturing', 'PCU324---324---'], ['Chemical mfg Chemical mfg', 'PCU325---325---'], ['Plastics and rubber products mfg Plastics and rubber products mfg', 'PCU326---326---'], ['Nonmetallic mineral product manufacturing Nonmetallic mineral product manufacturing', 'PCU327---327---'], ['Primary metal mfg Primary metal mfg', 'PCU331---331---'], ['Fabricated metal product mfg Fabricated metal product mfg', 'PCU332---332---'], ['Machinery manufacturing Machinery manufacturing', 'PCU333---333---'], ['Computer & electronic product mfg Computer & electronic product mfg', 'PCU334---334---'], ['Electrical equipment  and appliance mfg Electrical equipment  and appliance mfg', 'PCU335---335---'], ['Transportation equipment manufacturing Transportation equipment manufacturing', 'PCU336---336---'], ['Furniture & related product mfg Furniture & related product mfg', 'PCU337---337---'], ['Medical equipment & supplies mfg Medical equipment & supplies mfg', 'PCU3391--3391--'], ['Merchant wholesalers, durable goods Merchant wholesalers, durable goods', 'PCU423---423---'], ['Merchant wholesalers, nondurable goods Merchant wholesalers, nondurable goods', 'PCU424---424---'], ['Motor vehicle and parts dealers Motor vehicle and parts dealers', 'PCU441---441---'], ['Furniture and home furnishings stores Furniture and home furnishings stores', 'PCU442---442---'], ['Electronics and appliance stores Electronics and appliance stores', 'PCU443---443---'], ['Building material and garden equipment and supply dealers Building material and garden equipment and supply dealers', 'PCU444---444---'], ['Food and beverage stores Food and beverage stores', 'PCU445---445---'], ['Health and personal care stores Health and personal care stores', 'PCU446---446---'], ['Gasoline stations Gasoline stations', 'PCU447---447---'], ['Clothing and clothing accessories stores Clothing and clothing accessories stores', 'PCU448---448---'], ['Sporting goods, hobby, and book stores Sporting goods, hobby, and book stores', 'PCU451---451---'], ['General merchandise stores General merchandise stores', 'PCU452---452---'], ['Nonstore retailers Nonstore retailers', 'PCU454---454---'], ['Air transportation Air transportation', 'PCU481---481---'], ['Rail transportation Rail transportation', 'PCU482---482---'], ['Water transportation Water transportation', 'PCU483---483---'], ['Truck transportation Truck transportation', 'PCU484---484---'], ['Transportation support activities Transportation support activities', 'PCU488---488---'], ['U.S. Postal Service U.S. Postal Service', 'PCU491---491---'], ['Warehousing and storage Warehousing and storage', 'PCU493---493---'], ['Couriers and messengers Couriers and messengers', 'PCU492---492---'], ['Publishing industries, except Internet Publishing industries, except Internet', 'PCU511---511---'], ['Broadcasting, except Internet Broadcasting, except Internet', 'PCU515---515---'], ['Telecommunications Telecommunications', 'PCU517---517---'], ['Security, commodity contracts and like activity Security, commodity contracts and like activity', 'PCU523---523---'], ['Insurance carriers and related activities Insurance carriers and related activities', 'PCU524---524---'], ['Hospitals Hospitals', 'PCU622---622---'], ['Accommodation Accommodation', 'PCU721---721---']]

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
    return years

def run(start="2003", end="2022"):
    out = {}
    for rows in dat:
        name = rows[0]
        item = retrieve(rows, start, end)
        out[name] = item
        print(item)
        print(name)

    with open("Industry_"+start+"-"+end+".json", "w") as outfile:
        json.dump(out, outfile)
