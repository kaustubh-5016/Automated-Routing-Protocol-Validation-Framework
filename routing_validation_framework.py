#!/usr/bin/env python3

"""
Automated Routing Protocol Validation Framework

Simulates virtual routers using Linux network namespaces
and validates route injection, convergence, and failure
scenarios for L2/L3 workflows.

Requires:
- Linux
- Python 3.8+
- Root privileges
"""

import subprocess
import time
import sys


class Router:
    def __init__(self, name):
        self.name = name

    def run(self, cmd):
        full_cmd = ["sudo", "ip", "netns", "exec", self.name] + cmd
        result = subprocess.run(full_cmd, capture_output=True, text=True)
        return result.stdout.strip()

    def create(self):
        subprocess.run(["sudo", "ip", "netns", "add", self.name], check=True)

    def delete(self):
        subprocess.run(["sudo", "ip", "netns", "del", self.name], check=False)

    def set_loopback(self):
        self.run(["ip", "link", "set", "lo", "up"])

    def add_interface(self, ifname):
        self.run(["ip", "link", "set", ifname, "up"])

    def assign_ip(self, ifname, ip):
        self.run(["ip", "addr", "add", ip, "dev", ifname])

    def add_route(self, network, via):
        self.run(["ip", "route", "add", network, "via", via])

    def del_route(self, network):
        self.run(["ip", "route", "del", network])

    def show_routes(self):
        return self.run(["ip", "route"])


class RoutingValidator:
    def __init__(self, router):
        self.router = router

    def validate_route(self, network, timeout=10):
        start_time = time.time()
        while time.time() - start_time < timeout:
            routes = self.router.show_routes()
            if network in routes:
                return True
            time.sleep(1)
        return False


def create_veth_pair(r1, r2, if1, if2):
    subprocess.run(
        ["sudo", "ip", "link", "add", if1, "type", "veth", "peer", "name", if2],
        check=True,
    )
    subprocess.run(["sudo", "ip", "link", "set", if1, "netns", r1.name], check=True)
    subprocess.run(["sudo", "ip", "link", "set", if2, "netns", r2.name], check=True)


def main():
    print("Starting Automated Routing Protocol Validation Framework...\n")

    r1 = Router("r1")
    r2 = Router("r2")

    # Cleanup if namespaces exist
    r1.delete()
    r2.delete()

    # Create routers
    r1.create()
    r2.create()

    r1.set_loopback()
    r2.set_loopback()

    # Create link between routers
    create_veth_pair(r1, r2, "veth-r1", "veth-r2")

    r1.add_interface("veth-r1")
    r2.add_interface("veth-r2")

    # Assign IPs
    r1.assign_ip("veth-r1", "192.168.1.1/24")
    r2.assign_ip("veth-r2", "192.168.1.2/24")

    # Inject route
    print("Injecting static route...")
    r1.add_route("10.10.10.0/24", "192.168.1.2")

    validator = RoutingValidator(r1)

    print("Validating route convergence...")
    if validator.validate_route("10.10.10.0/24"):
        print("Route validation SUCCESS")
    else:
        print("Route validation FAILED")

    # Simulate failure
    print("\nSimulating route withdrawal...")
    r1.del_route("10.10.10.0/24")

    time.sleep(2)

    if not validator.validate_route("10.10.10.0/24", timeout=3):
        print("Route withdrawal validation SUCCESS")
    else:
        print("Route withdrawal validation FAILED")

    print("\nCleaning up namespaces...")
    r1.delete()
    r2.delete()

    print("\nExecution complete.")


if __name__ == "__main__":
    if sys.platform != "linux":
        print("This framework runs only on Linux.")
        sys.exit(1)

    main()
