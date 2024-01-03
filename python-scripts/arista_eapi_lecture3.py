import requests
import json
from pprint import pprint
from getpass import getpass

from urllib3.exceptions import InsecureRequestWarning
import ipdb

requests.packages.urllib3.disable_warnings(category = InsecureRequestWarning)

if __name__ == "__main__":

    ipdb.set_trace()
    https_headers = {"Content-Type": "application/json-rpc;"}
    host = "arista8.lasthop.io"
    port = 443
    username = "pyclass"
    password = getpass()
    
    url = "https://{}:{}/command-api".format(host,port)

    json_payload = {
        "jsonrpc": "2.0",
        "method": "runCmds",
        "params": {"version": 1, "cmds": ["show version"], "format": "json"},
        "id" : "1",
    }
    
    json_data = json.dumps(json_payload)
    https_headers["Content-length"] = str(len(json_data))
    
    response = requests.post(
        url,
        headers=https_headers,
        auth=(username, password),
        data = json_data,
        verify = False,
    )

    response = response.json()

    print()
    print(response)
    print()


