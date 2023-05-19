circuit_info = {}
#circuit_info["ip_addr"] = "100.65.255.10/30"
circuit_info["ip_addr_wo_mask"] = "100.65.255.10"
while True:
    circuit_info["peer_ip"] = input(f"Enter abc\'s ip address without the mask:  ")
    temp_var = circuit_info["peer_ip"]
    temp_var = temp_var.split(".")
    temp_var2 = circuit_info["ip_addr_wo_mask"]
    temp_var2 = temp_var2.split(".")
    x = temp_var[:]
    x.pop(3)
    y = temp_var2[:]
    y.pop(3)
    if (x == y):
        temp_var = temp_var[3]
        temp_var2 = temp_var2[3]
        if (int(temp_var) + 1) == int(temp_var2):
            break
        else:
            print("The last octet of the peer ip is expected to odd and 1 less than interface(irb) ip")
    else:
         print("peer ip's first 3 octets dont match the interface's address")
