from netmiko import ConnectHandler
from getpass import getpass

net_connect = ConnectHandler(
        host = 'dfffw',
        username = 'vigneshn',
        password = getpass(),
        device_type = 'fortinet_ssh',
        session_log = 'my_session_dfffw.txt'
)

print(net_connect.find_prompt())

