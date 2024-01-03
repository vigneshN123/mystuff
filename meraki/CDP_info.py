import meraki
from pprint import pprint 


API_KEY = 'XXXXXXXXXX'

dashboard = meraki.DashboardAPI(API_KEY)

with open("AP_serial.txt") as f:
 data = f.read()
data = data.splitlines()

list_APS = []

for i in data:
    response = dashboard.devices.getDeviceLldpCdp(i)
    list_APS.append(response)
 

pprint(list_APS) 
