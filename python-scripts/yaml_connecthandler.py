
import yaml
from netmiko import ConnectHandler
from pprint import pprint

with open(".netmiko.yml", "r") as f:
    data = yaml.load(f, Loader = yaml.FullLoader)


print()
pprint(data)
print()

for key in data:
    if type(data[key]) == list:
        continue
    ssh = ConnectHandler(**data[key])
    print()
    print(ssh.find_prompt())
    ssh.disconnect()
    print()





