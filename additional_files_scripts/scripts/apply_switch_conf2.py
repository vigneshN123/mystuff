from netmiko import ConnectHandler
from pprint import pprint
from getpass import getpass
import datetime

user = input("Username: ")
passwd = getpass(prompt = "Password: ")


with open("au_switches.txt") as f:
        data = f.read()


d = data.splitlines()

for device in d:
    device_info = {
        'host' : device,
        'username' : user,
        'password' : passwd,
        'device_type' : 'juniper_junos',
        'session_log' : 'au_sw_log.txt',
        'session_log_file_mode' : 'append',
        'fast_cli' : True
        }

    print(f"{datetime.datetime.now()} Connecting to {device}...")
    ssh = ConnectHandler(**device_info)
    print(f"Connection established : {ssh.find_prompt()}")

    
    output = ssh.send_config_from_file(config_file = "commands.txt", exit_config_mode=False ,strip_prompt=False, strip_command=False)
    #print(output)
    
    print (f"{datetime.datetime.now()} Committing configuration to {device}")
    output2 = ssh.commit(comment='delete system archival and change root password', and_quit=True)
    #print(output2)
   
    print(f"Disconnecting from {device}...")
    ssh.disconnect()
    print(f"{datetime.datetime.now()} Disconnected!")
    print()

