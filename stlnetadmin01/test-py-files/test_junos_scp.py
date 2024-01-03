from netmiko import ConnectHandler, file_transfer, progress_bar
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

source_file = "dfjcore0-config"
dest_file = "dfjcore0-config1"
direction   = "get"
file_system = None

transfer_dict = file_transfer(ssh,source_file, dest_file,None,'get', overwrite_file = True, )

print(transfer_dict)

#print(progress_bar(dest_file, 31191, True))




