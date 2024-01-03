#!/usr/bin/python
import sys
#import os
from jinja2 import FileSystemLoader, StrictUndefined
from jinja2.environment import Environment
from pprint import pprint
import opencsvPhy
#import ipdb

#jinja2 template gluecode
env = Environment(undefined = StrictUndefined)
env.loader = FileSystemLoader(".")

#Create input args for jinja template
circuit_info = {}
circuit_info = opencsvPhy.line.copy()
#pprint(circuit_info)


#Make python recognize backspace
#os.system("stty erase '^H'")

#ipdb.set_trace()

#Receive input from user
#input for location
if circuit_info['location'] == "au" or circuit_info['location'] == "sf":
     pass
else:
     print("Incorrect value for location please edit csv file. Input is casesentive: au or sf")
     sys.exit()

temp_var = list(circuit_info['intf'])
if (len(temp_var) == 8 or len(temp_var) == 9) and (temp_var[0] == "g" or temp_var[0] == "x") and (temp_var[1]== "e") and (temp_var[2] == "-" and temp_var[4] == "/" and temp_var[6] == "/"):
     pass
else:
     print("Incorrect interface name! please ensure interface name matches junos syntax (for example ge-0/0/1 or xe-0/2/1) ")
     sys.exit()

if (1740 <= int(circuit_info['vlan_id']) <= 1900):
     pass
else:
     print("vlan id not in the range 1740-1900 please re-enter vlan id:")
     sys.exit()

temp_var = circuit_info["ip_addr"]
temp_var = temp_var.split(".")
if (temp_var[0]=="100" and temp_var[1]=="65" and (250 <= int(temp_var[2]) <= 255)):
     temp_var = temp_var[3].split("/")
     if ((int(temp_var[0]) % 2 == 0) and (29 <= int(temp_var[1]) <= 30)):
         pass
     elif ((int(temp_var[0]) % 2 != 0)  and (29 <= int(temp_var[1]) <= 30)):
         print("The last octet of the ip address is expected to be even in number")
         sys.exit()
     elif ((int(temp_var[0]) % 2 == 0) and (not (29 <= int(temp_var[1]) <= 30))):
         print("The mask used is not to be greater than 30 and less than 29")
         sys.exit()
     else:
         print("Incorrect value for last octet and mask")
         sys.exit()
else:
     print("Incorrect address! re-enter the interface ip address")
     sys.exit()

# Extract just the ip without mask from the previous input
tmp_var = circuit_info["ip_addr"]
tmp_var = tmp_var.split(".")
x = tmp_var[3]
x = x.split("/")
tmp_var.pop(3)
tmp_var.insert(3, x[0])
circuit_info["ip_addr_wo_mask"] = ".".join(tmp_var)

temp_var = circuit_info["peer_ip"]
temp_var = temp_var.split(".")
temp_var2 = circuit_info["ip_addr_wo_mask"]
temp_var2 = temp_var2.split(".")
x = temp_var[:]
x.pop(3)
y = temp_var2[:]
y.pop(3)
if (x == y):
     temp_var = temp_var[3]
     temp_var2 = temp_var2[3]
     if (int(temp_var) + 1) == int(temp_var2):
         pass
     else:
         print("The last octet of the peer ip is expected to odd and 1 less than interface(irb) ip")
         sys.exit()
else:
     print("peer ip's first 3 octets dont match the interface's address")
     sys.exit()

circuit_info['prfx_list'] = circuit_info['prefx_list '].split(",")
circuit_info.pop('prefx_list ')

pprint(circuit_info)


#choose the jinja template file
template = env.get_template("CCS5-physical.j2")
#create the config from jinja template file
config = template.render(**circuit_info)

print()
print()
print(f"Physical interface and routing config for customer {circuit_info['customer']} is :")
print(config)
