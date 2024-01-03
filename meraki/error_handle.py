import meraki
from pprint import pprint
import pdb

API_KEY = 'XXXXXXXXXX'

dashboard = meraki.DashboardAPI(API_KEY)

serial = 'Q2HY-7S6E-RGKL'

#pdb.set_trace()

try:
    response = dashboard.devices.getDeviceLldpCdp(serial)
except ValueError as e:
    print(e.status)
    print(e.reason)
    print(e.message)
