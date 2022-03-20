from netmiko import ConnectHandler
from getpass import getpass


cisco4 = {
'host' : 'cisco4.lasthop.io',
'username' : 'pyclass',
'password' : getpass(),
'device_type' : 'cisco_ios_ssh',
'session_log' : 'cisco4_ping2.txt',
'fast_cli' : True
}


ssh = ConnectHandler(**cisco4)
print(ssh.find_prompt())

out = ssh.send_command("ping", expect_string = r':',strip_prompt = False, strip_command = False)
out += ssh.send_command("", expect_string = r':',strip_prompt = False, strip_command = False)
out += ssh.send_command("8.8.8.8", expect_string = r':',strip_prompt = False, strip_command = False)
out += ssh.send_command("", expect_string = r':',strip_prompt = False, strip_command = False)
out += ssh.send_command("", expect_string = r':',strip_prompt = False, strip_command = False)
out += ssh.send_command("", expect_string = r':',strip_prompt = False, strip_command = False)
out += ssh.send_command("", expect_string = r':',strip_prompt = False, strip_command = False)
out += ssh.send_command("", expect_string = r':',strip_prompt = False, strip_command = False)

print(out)

ssh.disconnect()


