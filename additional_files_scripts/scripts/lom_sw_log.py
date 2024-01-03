from netmiko import ConnectHandler
from getpass import getpass
from pprint import pprint
import datetime

username = input("Enter ssh username: ")
password = getpass(prompt = f"Enter ssh password for {username}: ")

with open("sf2_lom_switches.txt") as f:
    data = f.read()

data = data.splitlines()

#pprint(data)

for d in data:
    device_info = {
        "host": d,
        "username": username,
        "password": password,
        "device_type" : 'juniper_junos',
        'session_log' : 'sf_sw_log.txt',
        'session_log_file_mode' : 'write',
        'fast_cli' : True
    }

    ssh = ConnectHandler(**device_info)
    print(f"{datetime.datetime.now()} conecting to {d} : {ssh.find_prompt()}")

    print(f"{datetime.datetime.now()} applying netconf config to {d}")
    ssh.send_config_from_file(config_file = "ignore_log.txt", strip_prompt=False, strip_command=False, cmd_verify=True, exit_config_mode=False)

    print(f"{datetime.datetime.now()} committing the config on {d}")
    ssh.commit(comment = "log statements to ignore from local and remote", and_quit = True)

    print(f"{datetime.datetime.now()} Disconnecting from {d}")
    ssh.disconnect()
    print(f"{datetime.datetime.now()} disconnected..")
    print()


