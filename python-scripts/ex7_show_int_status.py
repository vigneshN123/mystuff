import textfsm
from pprint import pprint

with open("sh_int_status.txt","r") as f:
    text = f.read()

template = open("sh_int_status.template")

re_table = textfsm.TextFSM(template)

data = re_table.ParseText(text)

template.close()

pprint(data)

tempdict = {}
lst_port_details = []

for i in data:
    tempdict['PORT_NAME'] = i[0]
    tempdict['STATUS'] = i[1]
    tempdict['VLAN'] = i[2]
    tempdict['DUPLEX'] = i[3]
    tempdict['SPEED'] = i[4]
    tempdict['PORT_TYPE'] = i[5]
    lst_port_details.append(tempdict)

print("new data struct of show int status is : ")
pprint(lst_port_details)
print()

 
