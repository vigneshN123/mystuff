from netmiko import ConnectHandler
from getpass import getpass
from pprint import pprint
import datetime

username = input("Enter ssh username: ")
password = getpass(prompt = f"Enter ssh password for {username}: ")

with open("au2_switches.txt") as f:
    data = f.read()

data = data.splitlines()

#pprint(data)

for d in data:
    device_info = {
        "host": d,
        "username": username,
        "password": password,
        "device_type" : 'juniper_junos',
        'session_log' : 'au_sw_log.txt',
        'session_log_file_mode' : 'write',
        'fast_cli' : True
    }

    ssh = ConnectHandler(**device_info)
    print(f"{datetime.datetime.now()} conecting to {d} : {ssh.find_prompt()}")

    print(f"{datetime.datetime.now()} applying netconf config to {d}")
    ssh.send_config_from_file(config_file = "commands_junos.txt", strip_prompt=False, strip_command=False, cmd_verify=True, exit_config_mode=False)

    print(f"{datetime.datetime.now()} committing the config on {d}")
    ssh.commit(comment = "snmp statements to ignore vme0 intf", and_quit = True)

    print(f"{datetime.datetime.now()} Disconnecting from {d}")
    ssh.disconnect()
    print(f"{datetime.datetime.now()} disconnected..")
    print()


