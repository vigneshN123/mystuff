from jinja2 import StrictUndefined, FileSystemLoader
from jinja2.environment import Environment
#import my_devices
#from netmiko import ConnectionHandler

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

for dev in list_devices:
    output = template.render(**dev)
    print(output)


    
