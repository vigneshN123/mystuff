from netmiko import ConnectHandler
from getpass import getpass

dfjcore0 = {
        "host" : "dfjcore0",
        "username" : "vigneshn",
        "password" : getpass(),
        "device_type": "juniper_junos_ssh",
        "session_log" : 'dfjcore0_$(date +%Y%m%d)_log.txt',
        "global_delay_factor" : 2
}

net_con = ConnectHandler(**dfjcore0)
print(net_con.find_prompt())

out = net_con.send_command("show configuration | display set | save /var/tmp/dfjcore0-config", expect_string = r'>', strip_prompt = False, strip_command = False)

out += net_con.send_command("file copy /var/tmp/dfjcore0-config scp://vigneshn@192.168.129.230/tftpboot/config/df/dfjcore0-config",expect_string = r'password:', strip_prompt = False, strip_command = False)

out += net_con.send_command_timing('Batw1ngs-Adm1n1!', delay_factor = 4, strip_prompt = False, strip_command = False)

print(out)


