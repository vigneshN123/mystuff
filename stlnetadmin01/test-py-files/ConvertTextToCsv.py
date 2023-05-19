# Custom script to break down vlanid text to 4 element list
from pprint import pprint
import csv


with open("vlanid_au.txt", "r") as f:
    fdata = f.read()


fdata = fdata.splitlines()
nlist = []

for line in fdata:
    line = line.split(maxsplit = 4)
    nlist.append(line)
    #print(f"{nlist}")
    #break

print(nlist)

for i in nlist:
    if (len(i) < 4):
        print(i)
        pass
    else:
        print(f"{i[0]},{i[1]},AU,AU CCS VLAN,Vail Data Center, active,{i[3:]}")

