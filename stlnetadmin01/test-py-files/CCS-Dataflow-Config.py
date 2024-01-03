#!/usr/bin/python
#import sys
#import os
from jinja2 import FileSystemLoader, StrictUndefined
from jinja2.environment import Environment
from pprint import pprint
#import ipdb
import opencsv

#jinja2 template gluecode
env = Environment(undefined = StrictUndefined)
env.loader = FileSystemLoader("/home/vigneshn/test-py-files")

#Create input args for jinja template
customer_ccs_info = {}

customer_ccs_info = opencsv.line.copy()
customer_ccs_info['cust_rtp_ip_list'] = customer_ccs_info['cust_rtp_ip_list'].split(",")
customer_ccs_info['cust_sip_ip_list'] = customer_ccs_info['cust_sip_ip_list'].split(",")
customer_ccs_info['vail_ip_list'] = customer_ccs_info['vail_ip_list'].split(",")
#sys.exit()

#choose the jinja template file
template = env.get_template("CCS-dataflows-2.j2")
#create the config from jinja template file
config = template.render(**customer_ccs_info)

print()
print()
print(f"Data flows for {customer_ccs_info['customer']} is :")
print(config)

