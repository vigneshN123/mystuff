from jnpr.junos import Device
from getpass import getpass
from pprint import pprint

dev1 = {"host": "dfjcore0",
        "username": "vigneshn",
        "password": getpass()}


j_dev1 = Device(**dev1)

#Connect to junos
j_dev1.open()


pprint(j_dev1.facts)


