from netmiko import ConnectHandler
from pprint import pprint
from getpass import getpass
import datetime

user = input("Username: ")
passwd = getpass(prompt = "Password: ")

commands = ["delete system archival", "delete system ntp server 172.20.4.10", "delete system ntp server 172.20.4.11", "commit"]

with open("sf_edge_switches.txt") as f:
        data = f.read()

#:print(data)

d = data.splitlines()

for device in d:
    device_info = {
        'host' : device,
        'username' : user,
        'password' : passwd,
        'device_type' : 'juniper_junos',
        'session_log' : 'sf_lomsw_log.txt',
        'session_log_file_mode' : 'append'
        }

    print(f"{datetime.datetime.now()} Connecting to {device}...")
    ssh = ConnectHandler(**device_info)
    print(f"Connection established : {ssh.find_prompt()}")
    output = ssh.send_config_set(commands, strip_prompt=False, strip_command=False)
    print(output)
    print(f"Disconnecting from {device}...")
    ssh.disconnect()
    print("datetime.datetime.now() Disconnected!")
    print()



