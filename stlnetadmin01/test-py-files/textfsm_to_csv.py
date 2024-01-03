from pprint import pprint
import textfsm
import ipdb

template_file = "au_prefix_file.fsm"
template = open(template_file)

with open("vlanid_au.txt", 'r') as f:
    fdata = f.read()

#ipdb.set_trace()

prfx_template = textfsm.TextFSM(template)
selected_data = prfx_template.ParseText(fdata)

pprint(selected_data)

template.close()

# loop thro list and generate CSV file
for i in selected_data:
    #print(i)
    print(f"{i[2]},active,{i[3]},Vail Data Center,AU,{i[0]},AU VLAN")



