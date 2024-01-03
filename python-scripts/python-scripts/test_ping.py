from netmiko import ConnectHandler
from getpass import getpass

cisco4 = {
        'host' : "cisco4.lasthop.io",
        'username' : "pyclass",
        'password' : getpass(),
        'device_type' : "cisco_ios_ssh",
        'session_log' : "cisco4_ping.txt"
}

ssh = ConnectHandler(**cisco4)
print(ssh.find_prompt())

out = ssh.send_command_timing("ping", strip_prompt = False, strip_command = False)
out += ssh.send_command_timing("\n ", strip_prompt = False, strip_command = False)
out += ssh.send_command_timing("8.8.8.8", strip_prompt = False, strip_command = False)
out += ssh.send_command_timing("", strip_prompt = False, strip_command = False)
out += ssh.send_command_timing("", strip_prompt = False, strip_command = False)
out += ssh.send_command_timing("", strip_prompt = False, strip_command = False)
out += ssh.send_command_timing("", strip_prompt = False, strip_command = False)
out += ssh.send_command_timing("", strip_prompt = False, strip_command = False)


print(out)
#print(out1)

ssh.disconnect()

