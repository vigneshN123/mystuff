data_flow file input format


SAMPLE INPUT:
location,customer,ticket_info,cust_rtp_ip_list,cust_sip_ip_list,vail_ip_list
au,unm,FW-4694,"8.48.174.200/29,8.48.174.192/29","8.48.174.201/32,8.48.174.193/32",8.28.65.106/31


# The first row defines the fields of input separated by commas. The following will indicate sample inputs
# - location : au or sf
# - customer : requires the abbreviated name (case insenstive) of the customer (info normally in the netadmin/ops ticket) FOR EXAMPLE: vrnt for verint
# - ticket_info : Firewall ticket number (info available the firewall ticket) FOR EXAMPLE : FW-1234
# - cust_rtp_ip_list : rtp subnets for customer to be entered in "" separated by , if there is more than 1 subnet (info available in the OPS ticket) FOR EXAMPLE : "120.30.40.0/24,120.31.41.0/24"
# - cust_sip_ip_list : sip subnets for customer to be entered in "" separated by , if there is more than 1 subnet (info available in the OPS ticket) FOR EXAMPLE : "120.30.40.1/32,120.31.41.1/32"
# - vail_ip_list : sip server ips for vail CCS5 subnets. To be entered in "" separated by , if there is more than 1 subnet (info available in the OPS ticket) FOR EXAMPLE : 8.226.3.50/31

