from jinja2 import StrictUndefined, FileSystemLoader
from jinja2.environment import Environment
import my_devices
from netmiko import ConnectHandler
from pprint import pprint

env = Environment(undefined = StrictUndefined)

env.loader = FileSystemLoader(".")

dev1 = {
    "device" : "nxos1",
    "interface" : "Ethernet1/1",
    "ip" : "10.1.100.1",
    "mask" : "24",
    "local_as" : "22",
    "peer" : "10.1.100.2"
}

dev2 = {
    "device" : "nxos2",
    "interface" : "Ethernet1/1",
    "ip" : "10.1.100.2",
    "mask" : "24",
    "local_as" : "22",
    "peer" : "10.1.100.1"
}

list_devices = [dev1, dev2]

template = env.get_template("interface.j2")

#dev1_confg = template.render(**dev1)
#print(dev1_confg)
#quit()

my_devices.nxos1['jinja_var'] = dev1
my_devices.nxos2['jinja_var'] = dev2 

#pprint(my_devices.nxos1)
#pprint(my_devices.nxos2)


for dev in (my_devices.nxos1, my_devices.nxos2):
    jinja_var = dev.pop("jinja_var")
    print(jinja_var)
    config = template.render(**jinja_var)
    print()
    print(config)
    ssh = ConnectHandler(**dev)
    print()
    print(ssh.find_prompt())
    config = config.splitlines()
    print(config)
    print()
    out = ssh.send_config_set(config, strip_prompt=True, strip_command=True)
    print(out)
    ssh.disconnect()

    
for dev in (my_devices.nxos1, my_devices.nxos2):
    ssh = ConnectHandler(**dev)
    print(ssh.find_prompt())
    print()
    out = ssh.send_command("show ip bgp summary", strip_prompt=True, strip_command=True, use_textfsm=True)
    pprint(out)
    out = ssh.send_command_timing(f"ping {out[0]['bgp_neigh']}", delay_factor=3, strip_prompt=True, strip_command=True)
    print(out) 
    ssh.disconnect()
    


    
    


    
