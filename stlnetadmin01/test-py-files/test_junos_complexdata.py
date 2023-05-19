from netmiko import ConnectHandler
from getpass import getpass
from pprint import pprint

dfjcore0 = {
        'host' : "dfjcore0",
        'username' : "vigneshn",
        'password' : getpass(),
        'device_type' : 'juniper_junos_ssh',
        'session_log' : 'dfjcore0_scp.txt'
}

# Intialize the SSH connection to dfjcore0
ssh = ConnectHandler(**dfjcore0)
print(ssh.find_prompt())


out = ssh.send_command("show ospf neighbor", strip_prompt=False, strip_command=False, use_textfsm=True)

print()
pprint(out)
print()

for i in out:
    print(f"The neighor address on interface {i['interface']} is {i['address']} and is of state {i['state']}")



