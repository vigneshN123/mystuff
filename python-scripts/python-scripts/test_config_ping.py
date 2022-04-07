from netmiko import ConnectHandler
from getpass import getpass
from pprint import pprint
from datetime import datetime

cisco4 = {
        'host' : "cisco3.lasthop.io",
        'username' : "pyclass",
        'password' : getpass(),
        'device_type' : "cisco_ios_ssh",
        'session_log' : "cisco3_config_ping.txt",
        'fast_cli' : True
}

ssh = ConnectHandler(**cisco4)
print(ssh.find_prompt())

config_command = [ "ip name-server 1.1.1.1",
                  "ip name-server 1.0.0.1",
                  "ip domain-lookup"
                ]

print()
print(datetime.now())
out = ssh.send_config_set(config_command)
print(out)
print(datetime.now())


out = ssh.send_command("ping google.com", strip_prompt=False, strip_command=False)
print(out)

ssh.disconnect()


