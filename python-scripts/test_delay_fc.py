from netmiko import ConnectHandler
from getpass import getpass

nxos2 = {
        'host' : "nxos2.lasthop.io",
        'username' : "pyclass",
        'password' : "88newclass",
        'device_type' : "cisco_nxos_ssh",
        'session_log' : "nxos2_lldp.txt",
        'global_delay_factor' : 2
}

ssh = ConnectHandler(**nxos2)
print(ssh.find_prompt())

out = ssh.send_command("sh lldp neighbor detail", strip_prompt = False, strip_command = False)


print(out)

ssh.disconnect()


