circuit_info = {}
while True:
    circuit_info["is_prfx"]= input(f"Are the advertised prefixes by abc already known - yes or no :  ")
    if circuit_info["is_prfx"] == "yes":
        while True:
            try:
                total_prfx = int(input("Enter the total number of prefixes: "))
            except ValueError:
                print("Incorrect data type please type a integer value")
            else:
                if total_prfx < 0:
                    raise ValueError('Negative values not allowed!')
                else:
                    prfx_list = []
                    for i in range(total_prfx):
                        i = input(f"Enter address of prefix-{i} (use format network_address/mask): ")
                        prfx_list.append(i)
                print(f"the list of prefixes are {prfx_list}")
                circuit_info["prfx_list"] = prfx_list
                break
        break
    elif circuit_info["is_prfx"] == "no":
        break
    else:
        print("Incorrect response please type yes or no (case sensitive)")
