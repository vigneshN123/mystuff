from netmiko import ConnectHandler
from getpass import getpass
from pprint import pprint

cisco4 = {
        'host' : "cisco3.lasthop.io",
        'username' : "pyclass",
        'password' : getpass(),
        'device_type' : "cisco_ios_ssh",
        'session_log' : "cisco3_arp.txt"
}

ssh = ConnectHandler(**cisco4)
print(ssh.find_prompt())

out = ssh.send_command("sh ip arp", use_textfsm=True)

print(out)

new_list = []

for i in out:
    mac = i['mac']
    ip_add = i['address']
    intf = i['interface']
    dict1 = dict({'mac_addr' : mac, 'ip_addr' : ip_add, 'intterface' : intf})
    new_list.append(dict1)

pprint(new_list)

ssh.disconnect()


