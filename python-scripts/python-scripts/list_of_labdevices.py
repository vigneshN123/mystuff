from pprint import pprint
import yaml


cisco3 = {
    'device_name' : 'cisco3',
    'host' : 'cisco3.lasthop.io',
    'username' : 'vigneshn',
    'passwd' : 'password123'
}

cisco4 = { 
    'device_name' : 'cisco4',
    'host' : 'cisco4.lasthop.io',
    'username' : 'vigneshn',
    'passwd' : 'password123'
}

arista1 = { 
    'device_name' : 'arista1',
    'host' : 'arista1.lasthop.io',
    'username' : 'vigneshn',
    'passwd' : 'password123'
}

arista2 = { 
    'device_name' : 'arista2',
    'host' : 'arista2.lasthop.io',
    'username' : 'vigneshn',
    'passwd' : 'password123'
}

arista3 = { 
    'device_name' : 'arista3',
    'host' : 'arista3.lasthop.io',
    'username' : 'vigneshn',
    'passwd' : 'password123'
}


list_labdevices = [cisco3, cisco4, arista1, arista2, arista3]

print(f"List of lab devices is: \n")
pprint(list_labdevices)
print()

with open("yaml_file.yml", 'r+') as f:
    yaml.dump(list_labdevices,f,default_flow_style=False)
    f.seek(0)
    data = f.read()
    #data = open('yaml_file.yml', 'r')
    pprint(data)








