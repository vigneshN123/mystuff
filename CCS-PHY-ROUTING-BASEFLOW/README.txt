custinfo file input format:

SAMPLE INPUT :
location,customer,cirid,speed,intf,vlan_id,ip_addr,peer_ip,remote_as,is_prfx,total_prfx,prefx_list
au,unm,1234556,1Gbps,ge-0/0/2,1844,100.65.253.170/30,100.65.253.169,3549,yes,2,"10.10.10.10/32,10.10.10.11/32"

# The first row defines the fields of input separated by commas. The following will indicate sample inputs
# - location : au or sf
# - customer : requires the abbreviated name (case insenstive) of the customer (info normally in the netadmin/ops ticket) FOR EXAMPLE: vrnt for verint
# - cirid : circuit ID of the customer (info available the netadmin ticket) FOR EXAMPLE : FRO200696399
# - speed : circuit speed of uplink/xover (info available the netadmin ticket) FOR EXAMPLE : 1Gbps
# - intf : local physical interface name for juniper EX4300 (must start with ge or xe) (info available the netadmin ticket)  FOR EXAMPLE : ge-0/0/1
# - vlan_id : vlan id for CCS customer (must be in the range 1740-1900) (info available the netadmin ticket)  FOR EXAMPLE : 1823
# - ip_addr : local irb/vlan interface ip address with mask (must of the following format 10.65.[250-255].x/30 where x is an even number) FOR EXAMPLE : 100.65.255.10/30
# - peer_ip : ip address of remote peer without mask (must of the following format 10.65.[250-255].x where x is an odd number ie 1 less than local interface ip)  FOR EXAMPLE : 100.65.255.9
# - remote_as : remote ASN info for customer (info available the netadmin ticket) FOR EXAMPLE : 3459
# - is_prfx : yes or no . Are the prefix info for the customer already available. FOR EXAMPLE : yes
# - total_prfx : total number prefixes advertised by customer(info available the OPS ticket). FOR EXAMPLE: 2
# - prefx_list : list of prefixes adervtsied by customer to be entered in "" separted by , if there is more than 1. FOR EXAMPLE : "10.10.10.10/32,10.10.10.11/32,10.10.10.12/32"


