import ipaddress
import math

def calculate_subnet(hosts_required):
    # Add 2 for network & broadcast
    bits_needed = math.ceil(math.log2(hosts_required + 2))
    subnet_mask = 32 - bits_needed
    total_hosts = 2 ** bits_needed
    return subnet_mask, total_hosts

def get_next_network(current_network, new_prefix):
    return list(current_network.subnets(new_prefix=new_prefix))[0]

def main():
    base_network_input = input("Enter base network (e.g., 192.168.0.0/16): ")
    try:
        base_network = ipaddress.IPv4Network(base_network_input, strict=False)
    except ValueError:
        print("Invalid network. Try again.")
        return

    num_vlans = int(input("Enter number of VLANs you need: "))
    vlan_configs = []
    
    for i in range(num_vlans):
        hosts = int(input(f"Enter required hosts for VLAN {i+1}: "))
        vlan_configs.append({
            "hosts": hosts,
            "vlan_id": 10 * (i + 1)  # e.g., 10, 20, 30...
        })

    # Sort by host requirement (largest first to minimize fragmentation)
    vlan_configs.sort(key=lambda x: x["hosts"], reverse=True)

    current_ip = base_network.network_address
    used_networks = []

    for vlan in vlan_configs:
        subnet_mask, total_hosts = calculate_subnet(vlan["hosts"])
        new_subnet = ipaddress.IPv4Network((current_ip, subnet_mask), strict=False)
        vlan["subnet"] = str(new_subnet)
        vlan["prefix"] = subnet_mask
        vlan["usable_hosts"] = total_hosts - 2

        used_networks.append(new_subnet)
        current_ip = new_subnet.broadcast_address + 1

    print("\n📊 VLAN & Subnet Allocation")
    print("=" * 40)
    for vlan in vlan_configs:
        print(f"VLAN {vlan['vlan_id']}: Needs {vlan['hosts']} hosts → "
              f"Assigned subnet: {vlan['subnet']} "
              f"(Usable: {vlan['usable_hosts']})")
    print("=" * 40)

if __name__ == "__main__":
    main()

