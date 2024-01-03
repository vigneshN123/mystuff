#!/usr/bin/python

import sys
from jinja2 import FileSystemLoader, StrictUndefined
from jinja2.environment import Environment
from pprint import pprint
import opencsvnetbox


env = Environment(undefined = StrictUndefined)
env.loader = FileSystemLoader("/home/vigneshn/test-py-files")

prefixdata = {}
prefixdata = opencsvnetbox.line.copy()
pprint(prefixdata)


