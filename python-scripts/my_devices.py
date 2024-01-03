#nxos1 (NX-OSv Switch)
#    hostname = nxos1.lasthop.io
#    ssh_port = 22
#    nxapi_port = 8443
#    username = pyclass
#    password = 88newclass

#nxos2 (NX-OSv Switch)
#    hostname = nxos2.lasthop.io
#    ssh_port = 22
#    nxapi_port = 8443
#    username = pyclass
#    password = 88newclass

from getpass import getpass

passwd = getpass(prompt = 'Enter the device login password:')


nxos1 = {
    "host" : "nxos1.lasthop.io",
    "username" : "pyclass",
    "password" : passwd,
    "device_type" : "cisco_nxos_ssh",
    "session_log" : "nxos_config-2c.txt",
    'session_log_file_mode' : 'append'
}

nxos2 = {
    "host" : "nxos2.lasthop.io",
    "username" : "pyclass",
    "password" : passwd,
    "device_type" : "cisco_nxos_ssh",
    "session_log" : "nxos_config-2c.txt",
    'session_log_file_mode' : 'append'
}


#print(nxos1)
#print(nxos2)


