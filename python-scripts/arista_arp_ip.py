import json

from pprint import pprint

with open('arista_arp.json','r') as f:
    
    data = json.load(f)

print()
pprint(data)
print()

data = data['ipV4Neighbors']

dict_ip_arp = {}

for i in range(len(data)):
    dict_ip_arp[data[i]['address']] = data[i]['hwAddress']

print("The dictionary is {}".format(dict_ip_arp))


