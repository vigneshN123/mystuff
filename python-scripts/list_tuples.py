from ciscoconfparse import CiscoConfParse

with open("BGP.conf", "r") as f:
    read = f.read()
    parse = CiscoConfParse(read.splitlines())


neighbor = parse.find_objects(r"^\sneighbor")

ip_as = []

for i in neighbor:
    remote_as = i.re_search_children(r"remote-as")
    remote_as = remote_as[0].text
    remote_as = remote_as.split()
    neighbor_ip = i.text
    neighbor_ip = neighbor_ip.split()
    n_ip_as = (neighbor_ip[-1],remote_as[-1])
    print(n_ip_as)
    ip_as.append(n_ip_as)


print("BGP Peers: \n{}".format(ip_as))


