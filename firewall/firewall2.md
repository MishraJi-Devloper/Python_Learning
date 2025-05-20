# Simulated Firewall Rule Checker with Random IPs

This Python script simulates a firewall by generating random IP addresses and checking them against a set of predefined rules to determine if they should be **blocked** or **allowed**.

---

## 📦 Requirements

- Python 3.x (no additional libraries required)

---

## 🎯 Purpose

- To demonstrate how a basic firewall logic might be implemented.
- Useful for learning purposes, testing, or developing before integrating with real network tools.

---

## 🧠 Concepts Covered

- **Random IP generation**
- **Firewall rule dictionary**
- **Basic IP matching logic**
- **Simulation of network traffic and actions**

---

## 🚀 Usage

Run the script with:

```bash
python3 firewall_simulation.py
````

---
## 📂 File: `firewall_simulation.py`

```python
import random

def generate_random_ip():
    return f"192.168.1.{random.randint(0, 20)}"

def check_firewall_rules(ip, rules):
    return rules.get(ip, "allow")

def main():
    firewall_rules = {
        "192.168.1.1": "block",
        "192.168.1.4": "block",
        "192.168.1.9": "block",
        "192.168.1.13": "block",
        "192.168.1.16": "block",
        "192.168.1.19": "block",
    }

    print("Simulating firewall rule checks...\n")
    for _ in range(12):
        ip_address = generate_random_ip()
        action = check_firewall_rules(ip_address, firewall_rules)
        random_number = random.randint(0, 9999)
        print(f"IP: {ip_address}, Action: {action}, Random: {random_number}")

if __name__ == "__main__":
    main()
```

---

## 📝 Example Output

```
Simulating firewall rule checks...

IP: 192.168.1.13, Action: block, Random: 5032
IP: 192.168.1.6, Action: allow, Random: 8243
IP: 192.168.1.1, Action: block, Random: 1471
...
```



## 📌 Notes

* This is just a simulation — it doesn't actually block anything.
* You can modify the IP range or rule logic to test more complex scenarios.

```
---
