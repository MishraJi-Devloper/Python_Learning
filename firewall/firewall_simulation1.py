# we import random module to generate random ip address
import random

#Below code shows that gemerate random ip address
def generate_random_ip():
    return f"192.168.1.{random.randint(0, 20)}"

# Below the code says that how we define a firewall cheking function and rules to check the randomized 
def check_firewall_rules(ip, rules):
    for rule_ip, action in rules.items():
        if ip == rule_ip:
            return action
    return "allow"

# Below the codes defines the main function . In this function we defines dictionary firewall rules.This predefine rules we match to block as a action
def main():
    firewall_rules = {
        "192.168.1.1" : "block",
        "192.168.1.4" : "block",
        "192.168.1.9" : "block",
        "192.168.1.13" : "block",
        "192.168.1.16" : "block",
        "192.168.1.19" : "block",
    }

# Below  this we simulate to traffic by generating 12 random ip addresses and checking them against the firewall rules and then we finally print the ip address and the coressponding action 
    for _ in range(12):
        ip_address = generate_random_ip()
        action = check_firewall_rules(ip_address, firewall_rules)
        random_number = random.randint(0, 9999)
        print(f"IP: {ip_address}, Action: {action}, Random: {random_number}")

# Below the main gured 
if __name__ == "__main__":
    main()