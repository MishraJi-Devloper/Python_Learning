# Real-Time Firewall Using Scapy and IPTables

This Python script uses `scapy` to monitor real-time network traffic and `iptables` to block IP addresses that exceed a defined packet rate threshold. It's a basic example of a rate-limiting firewall system in Python.

---

## 🔧 Requirements

- Python 3.x
- Root privileges (sudo access)
- `scapy` library

Install `scapy` using pip:

```bash
pip install scapy

---

## ⚙️ How It Works

* The script uses `scapy` to sniff incoming IP packets.
* It tracks how many packets are received per IP address every second.
* If any IP exceeds the defined **packet threshold**, it gets blocked using an `iptables` rule.

---

## 🧠 Key Concepts

* `scapy.all.sniff`: Captures live network packets.
* `IP in packet`: Filters only IP packets.
* `iptables`: Linux firewall command to block network traffic.
* `os.geteuid()`: Checks if the script is running as root.

---

## 🚀 Usage

Run the script **with root privileges**:

```bash
sudo python3 firewall_real.py
```

---

## 🛡️ Warning

* This script **modifies your firewall rules**. Use with caution.
* Avoid testing on production systems or critical environments.
* You can flush the rules added using:

```bash
sudo iptables -F
```

---

## 🔄 Script Overview

```python
THRESHOLD = 40  # packets/sec

if os.geteuid() != 0:
    print("This script requires root privileges.")
    sys.exit(1)

sniff(filter="ip", prn=packet_callback)
```

---