from pprint import pprint

arp = """
Protocol  Address      Age  Hardware Addr   Type  Interface
Internet  10.220.88.1   67  0062.ec29.70fe  ARPA  Gi0/0/0
Internet  10.220.88.20  29  c89c.1dea.0eb6  ARPA  Gi0/0/0
Internet  10.220.88.22   -  a093.5141.b780  ARPA  Gi0/0/0
Internet  10.220.88.37 104  0001.00ff.0001  ARPA  Gi0/0/0
Internet  10.220.88.38 161  0002.00ff.0001  ARPA  Gi0/0/0
"""

arp = arp.strip()
arp_list = arp.splitlines()

processed_list = []

for arp_entry in arp_list:
    if arp_entry == "Protocol  Address      Age  Hardware Addr   Type  Interface":
        continue
    else:
        arp_entry = arp_entry.split()
        mac = arp_entry[3]
        ip = arp_entry[1]
        intf = arp_entry[5]
        dic1 = dict({'mac_addr' : mac, 'ip_addr': ip, 'interface' : intf})
        processed_list.append(dic1)


print(processed_list)

print()
pprint(processed_list)
print()



