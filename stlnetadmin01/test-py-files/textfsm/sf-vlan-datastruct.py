from pprint import pprint
import textfsm

template_file = "sf-vlan.fsm"
template = open(template_file)

with open("SF-VLAN.txt", "r") as f:
    fdata = f.read()

vlan_template = textfsm.TextFSM(template)
selected_data = vlan_template.ParseText(fdata)

#pprint(selected_data)

template.close()

for i in selected_data:
    print(f"{i[2]},Vail Data Center,SF (dc 1 and 2),SF VLAN,{i[0]},active,{i[3]}")
