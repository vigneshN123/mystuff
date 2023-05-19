from pprint import pprint
import textfsm

template_file = "CCS_to_textfsm.fsm"
template = open(template_file)

with open("ccs-data-updated1.csv", "r") as f:
    fdata = f.read()

ccs_template = textfsm.TextFSM(template)
selected_data = ccs_template.ParseText(fdata)

#pprint(selected_data)

template.close()
lenght = 0
for i in selected_data:
 if i[1] == "Aurora":
     print(f"{i[3]},Vail Data Center,AU, AU CCS VLAN,{i[2]},active,{i[4]}")
 else:
     print(f"{i[3]},Vail Data Center,SF (dc 1 and 2), SF CCS VLAN,{i[2]},active,{i[4]}")

