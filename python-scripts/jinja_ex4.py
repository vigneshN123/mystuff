from jinja2 import FileSystemLoader, StrictUndefined
from jinja2.environment import Environment 
from pprint import pprint

env = Environment(undefined = StrictUndefined)

env.loader = FileSystemLoader(".")

Total_vrf = int(input("Enter the number of Vrfs"))

vrf_names = []

for i in range(Total_vrf):
    name_vrf = input(f"Enter the name of vrf{i} : ")
    vrf_names.append(name_vrf)

print(vrf_names)

vrf_values = {
"vrf_name" : vrf_names,
#"id" : len(vrf_names),
"ipv4" : True,
"ipv6" : False
}

#pprint(vrf_values)

template_file = "vrf2.j2"

template = env.get_template(template_file)

output = template.render(**vrf_values)

print(output)




