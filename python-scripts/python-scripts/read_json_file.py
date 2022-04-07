import json
from pprint import pprint

with open('nxos_json.json', 'r') as f:
    data = json.load(f)
    #print(data)
    print()


pprint(data)
print()
print()
print()
print()


ipv4_list = []
ipv6_list = []

for k,v in data.items():
    for i,j in v.items():
        if i == 'ipv4':
            X = list(j.keys())
            Y = list(j.values())
            for i in range(len(X)):
                Z = str(X[i])+"/"+str(Y[i]['prefix_length'])
                ipv4_list.append(Z)
        else: 
            X = list(j.keys())
            Y = list(j.values())
            for i in range(len(X)):
                Z = str(X[i])+"/"+str(Y[i]['prefix_length'])
                ipv6_list.append(Z)


print(f"List of ipv4 addresses is: \n {ipv4_list}")
print()
print(f"List of ipv6 addresses is: \n {ipv6_list}")
print()

 
