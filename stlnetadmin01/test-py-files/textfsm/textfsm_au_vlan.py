from pprint import pprint
import textfsm

template_file = "vlan_to_csv.fsm"
template = open(template_file)

with open("vlanid_au.txt", "r") as f:
    fdata = f.read()

prfx_tmp = textfsm.TextFSM(template)
selected_data = prfx_tmp.ParseText(fdata)

pprint(selected_data)

template.close()

print("#")
print("#")

for i in selected_data:
    print(f"{i[1]},active,{i[2]},Vail Data Center,AU")
