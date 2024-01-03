#!/usr/bin/python
#import sys
import os
from jinja2 import FileSystemLoader, StrictUndefined
from jinja2.environment import Environment
from pprint import pprint
#import ipdb

#jinja2 template gluecode
env = Environment(undefined = StrictUndefined)
env.loader = FileSystemLoader("/home/vigneshn/test-py-files")

#Create input args for jinja template
circuit_info = {}

#Make python recognize backspace
os.system("stty erase '^H'")

#ipdb.set_trace()

#Receive input from user
#input for location
while True:
    circuit_info['location'] = input("Enter the location of the xover - au or sf : ")
    if circuit_info['location'] == "au" or circuit_info['location'] == "sf":
        break
    else:
        print("Incorrect answer please choose between au or sf")

#input for customer name
circuit_info['customer'] = input("Enter the customer name acronym(in lower case): ")
#input for customer circuit id
circuit_info['cirid'] = input("Enter the circuit id: ")
#input for circuit Bandwidth
circuit_info['speed'] = input("Enter circuit speed in Gbps (for example 1Gbps): ")
#input for uplink switch interface name
while True:
    circuit_info['intf'] = input("Enter ex switch interface name (for example ge-0/0/1 or xe-0/2/1) : ")
    temp_var = list(circuit_info['intf'])
    if (len(temp_var) == 8 or len(temp_var) == 9) and (temp_var[0] == "g" or temp_var[0] == "x") and (temp_var[1]== "e") and (temp_var[2] == "-" and temp_var[4] == "/" and temp_var[6] == "/"):
        break
    else:
        print("Incorrect interface name! Please try again..")
#input for vlan id info
while True:
    circuit_info['vlan_id'] = int(input("Enter the vlan id : "))
    if (1740 <= circuit_info['vlan_id'] <= 1900):
        break
    else:
        print("vlan id not in the range 1740-1900 please re-enter vlan id:")
#input for switch vlan interface ip address
# use regex to look for mask
while True:
    circuit_info["ip_addr"] = input("Enter the vlan (irb) interface ip address with mask (for example 100.65.254.222/30): ")
    temp_var = circuit_info["ip_addr"]
    temp_var = temp_var.split(".")
    if (temp_var[0]=="100" and temp_var[1]=="65" and (250 <= int(temp_var[2]) <= 255)):
        temp_var = temp_var[3].split("/")
        if ((int(temp_var[0]) % 2 == 0)  and (29 <= int(temp_var[1]) <= 30)):
            break
        elif ((int(temp_var[0]) % 2 != 0)  and (29 <= int(temp_var[1]) <= 30)):
            print("The last octet of the ip address is expected to be even in number")
        elif ((int(temp_var[0]) % 2 == 0)  and (not (29 <= int(temp_var[1]) <= 30))):
            print("The mask used is not to be greater than 30 and less than 29")
        else:
            print("Incorrect value for last octet and mask")
    else:
        print("Incorrect address! re-enter the interface ip address")

#Extract just the ip without mask from the previous input
tmp_var = circuit_info["ip_addr"]
tmp_var = tmp_var.split(".")
x = tmp_var[3]
x = x.split("/")
tmp_var.pop(3)
tmp_var.insert(3,x[0])
circuit_info["ip_addr_wo_mask"] =".".join(tmp_var)

#input for peer ip address without mask
while True:
    #ipdb.set_trace()
    circuit_info["peer_ip"] = input(f"Enter { circuit_info['customer']  }\'s ip address w/o the mask:  ")
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
            break
        else:
            print("The last octet of the peer ip is expected to odd and 1 less than interface(irb) ip")
    else:
        print("peer ip's first 3 octets dont match the interface's address")

#input for peer asn
circuit_info['remote_as'] = input("Enter remote AS number:  ")

#input for peer prefixes
while True:
    circuit_info["is_prfx"]= input(f"Are the advertised prefixes by {circuit_info['customer']} already known - yes or no :  ")
    if circuit_info["is_prfx"] == "yes":
        while True:
            try:
                total_prfx = int(input("Enter the total number of prefixes: "))
            except ValueError:
                print("Incorrect data type please type a integer value")
            else:
                prfx_list = []
                for i in range(total_prfx):
                    i = input(f"Enter address of prefix-{i} (use format network_address/mask): ")
                    prfx_list.append(i)
                print(f"the list of prefixes are {prfx_list}")
                circuit_info["prfx_list"] = prfx_list
                break
        break
    elif circuit_info["is_prfx"] == "no":
        break
    else:
        print("Incorrect response please type yes or no (case sensitive)")

#choose the jinja template file
template = env.get_template("CCS-physical.j2")
#create the config from jinja template file
config = template.render(**circuit_info)

print()
print()
print(f"Physical interface and routing config for customer {circuit_info['customer']} is :")
print(config)
