from netmiko import ConnectHandler
from getpass import getpass
import datetime

nxos2 = {
        'host' : "nxos2.lasthop.io",
        'username' : "pyclass",
        'password' : "88newclass",
        'device_type' : "cisco_nxos_ssh",
        'session_log' : "nxos2_lldp2.txt",
        'global_delay_factor' : 2
}

ssh = ConnectHandler(**nxos2)
print(ssh.find_prompt())

print()
print(datetime.datetime.now())
print()
out = ssh.send_command("sh lldp neighbor detail")
print(out)
print()
print(datetime.datetime.now())
print()

print()
print(datetime.datetime.now())
print()
out = ssh.send_command("sh lldp neighbor detail", delay_factor = 8)
print(out)
print()
print(datetime.datetime.now())
print()
ssh.disconnect()
print('#'*20)
print()


