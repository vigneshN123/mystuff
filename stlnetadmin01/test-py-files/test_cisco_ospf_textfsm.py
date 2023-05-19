from netmiko import ConnectHandler
from getpass import getpass
from pprint import pprint

dfrcore01 = {
        "host" : "dfrcore01",
        "username" : "vigneshn",
        "password" : getpass(),
        "device_type" : "cisco_ios",
        "session_log" : "dfrcore0_log.txt",
        "global_delay_factor" : 2
}

con1 = ConnectHandler(**dfrcore01)

print(con1)

print(con1.find_prompt())

out = con1.send_command("sh ip ospf neighbor", use_textfsm = True, strip_prompt = False, strip_command = False)

print(out)
pprint(out)


con1.disconnect()

