from netmiko import ConnectHandler
from getpass import getpass

Firewall1 = {
        "host" : 'dfffw',
        "username" : 'vigneshn',
        "password" : getpass(),
        "device_type" : 'fortinet_ssh',
       # "global_delay_factor" : 0
        "session_log" : 'my_session_dfffw.txt'
}

net_connect = ConnectHandler(**Firewall1)
print(net_connect.find_prompt())

out = net_connect.send_command("get sys status")
print(out)
net_connect.disconnect()
