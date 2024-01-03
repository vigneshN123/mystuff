from netmiko import ConnectHandler
from getpass import getpass
from pprint import pprint

dfrcore01 = {
        'host' : "dfrcore01",
        'username' : "vigneshn",
        'password' : getpass(),
        'device_type' : "cisco_ios_ssh",
        'session_log' : "dfrcore01_config_change.txt",

}

ssh = ConnectHandler(**dfrcore01)
print(ssh.find_prompt())


#cfg = [ 
#        "int gi3/11",
#        "description test-interface"
#]

#output = ssh.send_config_set(cfg)


output = ssh.send_config_from_file("dfrcore01_config.txt")
print(output)

ssh.disconnect()

