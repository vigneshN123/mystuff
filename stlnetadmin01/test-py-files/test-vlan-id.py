circuit_info = {}
while True:
    try:
        circuit_info['vlan_id'] = int(input("Enter the vlan id : "))
    except ValueError:
        print("Please type integer data type")
    else:
        if (1740 <= int(circuit_info['vlan_id']) <= 1900):
            break
        else:
            print("vlan id not in the range 1740-1900 please re-enter vlan id:")
