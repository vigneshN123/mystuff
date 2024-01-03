from netmiko import ConnectHandler
from getpass import getpass

ExSwitch = {
        "host" : "dfjcore0",
        "username" : "vigneshn",
        "password" : getpass(),
        "device_type" : "juniper_junos",
        "session_log" : "dfjcore0_log.txt"
}

net_connect = ConnectHandler(**ExSwitch)
print(net_connect.find_prompt())

out = net_connect.send_command("show interface terse | match up | except down", expect_string = r'#')
print(out)


