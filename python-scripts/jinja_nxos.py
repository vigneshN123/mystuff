from jinja2 import FileSystemLoader, StrictUndefined
from jinja2.environment import Environment

env = Environment(undefined = StrictUndefined)
env.loader = FileSystemLoader('.')


var1 = {
    "device" : "nxos1",
    "interface" : "Ethernet1/1",
    "ip" : "10.1.100.1",
    "mask" : "24"
}

var2 = {
    "device" : "nxos2",
    "interface" : "Ethernet1/1",
    "ip" : "10.1.100.2",
    "mask" : "24"
}

template_file = 'interface.j2'

template = env.get_template(template_file)

output = template.render(**var1)

output += template.render(**var2)

print(output)


