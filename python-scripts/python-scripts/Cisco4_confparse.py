from netmiko import ConnectHandler
from getpass import getpass
from pprint import pprint
from ciscoconfparse import CiscoConfParse


cisco4 = {
        'host' : "cisco4.lasthop.io",
        'username' : "pyclass",
        'password' : getpass(),
        'device_type' : "cisco_ios_ssh",
        'session_log' : "cisco4_cisco_confparse.txt"
}

ssh = ConnectHandler(**cisco4)

print(f"Connected to device {cisco4['host']} : {ssh.find_prompt()}")
print()


out = ssh.send_command("sh run | sec interface", strip_prompt=False, strip_command=False)

print(out)
print()
print()

parse = CiscoConfParse(out.splitlines())

# locate interface with ip address

Intf_with_ip = parse.find_objects_w_all_children(r"^interface", ["^\sip address"])

print("Only interafce with IP is : {}".format(Intf_with_ip))
print()
print()

print(f"Interface line: {Intf_with_ip[0].text}") 
print(f"IP Address Line: {Intf_with_ip[0].children[0].text}")

