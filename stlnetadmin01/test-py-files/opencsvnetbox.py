import csv
from pprint import pprint
import ipdb

filename = "ccs-data-updated1.csv"

#ipdb.set_trace()

with open(filename, "r") as f:
    dict_reader = csv.DictReader(f)
    #pprint(dict_reader)
    list_of_dict = list(dict_reader)
    #pprint(list_of_dict)

for i in list_of_dict:
    if (i['Vail CCS Site'] == 'Aurora'):
        print(f"{i['Uplink VLAN ID']},au-ccs-dcc-{i['Customer'].lower()},AU,AU CCS VLAN,Vail Data Center,active,{i['Description']}")
    else:
        print(f"{i['Uplink VLAN ID']},sf-ccs-dcc-{i['Customer'].lower()},SF(dc 1 and 2),SF CCS VLAN,Vail Data Center,active,{i['Description']}")


