import os

def generate_juniper_ospf_config(router_id: str, interface_ip: str, interface_name: str) -> str:
    """
    Generates a basic Juniper OSPF configuration for a single router.

    Args:
        router_id (str): The OSPF router ID.
        interface_ip (str): The IP address for the interface (e.g., "192.168.1.1/24").
        interface_name (str): The name of the interface (e.g., "ge-0/0/0").

    Returns:
        str: The Juniper configuration as a string.
    """
    config = f"""
version 22.4R1.8;
host-name R{router_id};

interfaces {{
    {interface_name} {{
        unit 0 {{
            family inet {{
                address {interface_ip};
            }}
        }}
    }}
}}

routing-options {{
    router-id {router_id}.{router_id}.{router_id}.{router_id};
    autonomous-system 65000;
}}

protocols {{
    ospf {{
        area 0.0.0.0 {{
            interface {interface_name}.0;
        }}
    }}
}}

"""
    return config

def create_gns3_configs(output_dir: str = 'gns3_configs'):
    """
    Creates Juniper configuration files for R1 and R2 in the specified output directory.
    """
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # R1 Configuration
    r1_config = generate_juniper_ospf_config(
        router_id="1",
        interface_ip="192.168.1.1/24",
        interface_name="ge-0/0/0"
    )
    with open(os.path.join(output_dir, 'R1_juniper_config.txt'), 'w') as f:
        f.write(r1_config)
    print(f"Generated {os.path.join(output_dir, 'R1_juniper_config.txt')}")

    # R2 Configuration
    r2_config = generate_juniper_ospf_config(
        router_id="2",
        interface_ip="192.168.1.2/24",
        interface_name="ge-0/0/0"
    )
    with open(os.path.join(output_dir, 'R2_juniper_config.txt'), 'w') as f:
        f.write(r2_config)
    print(f"Generated {os.path.join(output_dir, 'R2_juniper_config.txt')}")

if __name__ == "__main__":
    create_gns3_configs()