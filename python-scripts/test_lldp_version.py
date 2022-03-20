from netmiko import ConnectHandler
from getpass import getpass
from pprint import pprint

cisco4 = {
        'host' : "cisco4.lasthop.io",
        'username' : "pyclass",
        'password' : getpass(),
        'device_type' : "cisco_ios_ssh",
        'session_log' : "cisco4_lldp_version.txt"
}

ssh = ConnectHandler(**cisco4)
print(ssh.find_prompt())

out1 = ssh.send_command("sh version", use_textfsm = True)

out2 = ssh.send_command("sh lldp neighbors", use_textfsm = True)

pprint(out1)
print()
print()
pprint(out2)
print()

for i in out2:
    print(f"the remote interface is  {i['neighbor_interface']}")

ssh.disconnect()


