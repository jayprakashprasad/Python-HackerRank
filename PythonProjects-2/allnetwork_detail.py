import psutil
from tabulate import tabulate


class Network_Details(object):
    def __init__(self):
        self.parser = psutil.net_if_addrs()


    def __repr__(self):
        self.address_ip = []
        self.network_ip = []
        self.interfaces = []
        self.broadcast_ip = []

        for interface_name, interface_addresses in self.parser.items():
            self.interfaces.append(interface_name)
            for address in  interface_addresses:
              if str(address.family) == 'AddressFamily.AF_INET':
                self.address_ip.append(address.address)
                self.network_ip.append(address.netmask)
                self.broadcast_ip.append(address.broadcast)

        data = { "Ip-address" : [*self.address_ip] ,
                "network" :     [*self.network_ip] ,
                "Interfaces" :  [*self.interfaces] ,
                "broadcast" :   [*self.broadcast_ip]
                 }
        return tabulate(data, headers ='keys',tablefmt='github')


if __name__ == "__main__":
    print(Network_Details())