from jinja2 import StrictUndefined, FileSystemLoader
from jinja2.environment import Environment
from pprint import pprint

env = Environment(undefined = StrictUndefined)
env.loader = FileSystemLoader(".")

vrf_var = {
"vrf_name" : "blue",
"id" : 1,
"ipv4" : True,
"ipv6" : False
}

template = env.get_template("vrf.j2")

vrf_confg = template.render(**vrf_var)

print(vrf_confg)


