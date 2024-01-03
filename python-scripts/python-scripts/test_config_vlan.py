from netmiko import ConnectHandler
from getpass import getpass
from pprint import pprint
from datetime import datetime



def main(out):
      print()
      print(f"Device name : {device}")
      print("Config applied is : /n")
      print(out)
      print()



nxos1 = {
        'host' : "nxos1.lasthop.io",
        'username' : "pyclass",
        'password' : getpass(),
        'device_type' : "cisco_nxos_ssh",
        'session_log' : "nxos_config_vlan.txt",
        'session_log_file_mode' : 'append',
        'fast_cli' : True
}
nxos2 = {
        'host' : "nxos2.lasthop.io",
        'username' : "pyclass",
        'password' : getpass(),
        'device_type' : "cisco_nxos_ssh",
        'session_log' : "nxos_config_vlan.txt",
        'session_log_file_mode' : 'append',
        'fast_cli' : True
}

n = [nxos1,nxos2]

for device in n:
    ssh = ConnectHandler(**device)
    print(ssh.find_prompt())
    out = ssh.send_config_from_file("vlan_config.txt")
    out += ssh.save_config()
    main(out)
    ssh.disconnect()


if __name__ == "__main__":
    main(out)



