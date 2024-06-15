def network(servers):
    result = ""
    for hostname, IP_address in servers.items():
        result += "The IP address of the {} server is {}".informat(hostname, IP_address) + "\n"
    return result
