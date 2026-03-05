# NmapBot

NmapBot is a **natural language interface for Nmap**.  
Users can type simple sentences instead of memorizing Nmap commands.

---

## Installation

```bash
git clone https://github.com/YourUsername/NmapBot.git
cd NmapBot
bash install.sh


---

Launch

nmapbot


---

Natural Language Commands

Sentence	Action

check open ports on TARGET	Basic TCP scan
run stealth scan on TARGET	SYN stealth scan
run connect scan on TARGET	TCP connect scan
scan TARGET using udp	UDP scan
scan all ports on TARGET	Full port scan
scan TARGET for services	Service version detection
find operating system of TARGET	OS detection
run aggressive scan on TARGET	Aggressive scan
check vulnerabilities on TARGET	Run NSE vuln scripts
discover devices on TARGET	Network discovery
trace route to TARGET	Traceroute
help	Show all commands
exit	Quit NmapBot



---

Example Usage

nmapbot
check open ports on scanme.nmap.org
run stealth scan on example.com
scan example.com for services
find operating system of example.com
check vulnerabilities on example.com
discover devices on 192.168.1.0/24
trace route to example.com
run aggressive scan on example.com
exit


---

Folder Structure

NmapBot/
├─ nmapbot.py
├─ install.sh
├─ reports/
├─ profiles/
├─ scripts/
├─ README.md
└─ requirements.txt


---

Requirements

Python 3

Nmap

Termux or Linux terminal

Python libraries: colorama, termcolor, prettytable



---

License

MIT License

---

## **4️⃣ requirements.txt**

colorama prettytable termcolor

---

## **5️⃣ .gitignore**

reports/ pycache/ *.pyc

---

✅ **How to use after pushing to GitHub:**

```bash
git clone https://github.com/YourUsername/NmapBot.git
cd NmapBot
bash install.sh
nmapbot.

IF ABOVE DOES NOT WORK, COPY PASTE THE BELOW ENTIRE SCRIPT AND HIT THE ENTER KEY. AND IT WILL INSTALL THE TOOL.

TO RUN THE TOOL TYPE "nmapbot"

Script:

cd ~
mkdir -p NmapBot && cd NmapBot

# Create installer script
cat << 'EOF' > install.sh
#!/bin/bash
echo "Installing NmapBot..."

# Update and install dependencies
pkg update -y && pkg upgrade -y
pkg install python nmap git wget -y
pip install colorama prettytable termcolor

# Create main Python script
cat << 'EOPY' > nmapbot.py
#!/usr/bin/env python3

import subprocess, socket, sys, re
from colorama import Fore, Style
from termcolor import colored
from prettytable import PrettyTable
import os
import datetime

REPORT_DIR = "reports"
os.makedirs(REPORT_DIR, exist_ok=True)

def resolve(target):
    try:
        return socket.gethostbyname(target)
    except:
        return target

def run_nmap(flags, target):
    ip = resolve(target)
    print(colored(f"\nTarget: {target}", "cyan"))
    print(colored(f"Resolved IP: {ip}\n", "cyan"))
    cmd = ["nmap"] + flags + [target]
    print(colored("Executing: " + " ".join(cmd), "yellow"))
    subprocess.run(cmd)
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"{REPORT_DIR}/scan_{target}_{timestamp}.txt"
    with open(filename, "w") as f:
        f.write(" ".join(cmd) + "\n")
    print(colored(f"\nReport saved: {filename}\n", "green"))

def parse_command(command):
    command = command.lower()
    target_match = re.search(r"(on|of|to)\s+([a-zA-Z0-9\.\-\/]+)", command)
    if not target_match:
        print(colored("⚠ Could not detect target.", "red"))
        return
    target = target_match.group(2)

    # Natural language command mapping
    if "open ports" in command: run_nmap([], target)
    elif "stealth" in command or "syn scan" in command: run_nmap(["-sS"], target)
    elif "connect scan" in command: run_nmap(["-sT"], target)
    elif "udp" in command: run_nmap(["-sU"], target)
    elif "all ports" in command: run_nmap(["-p-"], target)
    elif "services" in command or "service version" in command: run_nmap(["-sV"], target)
    elif "operating system" in command or "os" in command: run_nmap(["-O"], target)
    elif "aggressive" in command: run_nmap(["-A"], target)
    elif "vulnerabilities" in command or "vuln" in command: run_nmap(["--script","vuln"], target)
    elif "discover" in command or "find devices" in command: run_nmap(["-sn"], target)
    elif "trace route" in command or "traceroute" in command: run_nmap(["--traceroute"], target)
    else:
        print(colored("⚠ Command not recognized.", "red"))

def help_menu():
    table = PrettyTable()
    table.field_names = ["Sentence", "Action"]
    table.add_row(["check open ports on TARGET", "Basic TCP scan"])
    table.add_row(["run stealth scan on TARGET", "SYN stealth scan"])
    table.add_row(["run connect scan on TARGET", "TCP connect scan"])
    table.add_row(["scan TARGET using udp", "UDP scan"])
    table.add_row(["scan all ports on TARGET", "Full port scan"])
    table.add_row(["scan TARGET for services", "Service version detection"])
    table.add_row(["find operating system of TARGET", "OS detection"])
    table.add_row(["run aggressive scan on TARGET", "Aggressive scan"])
    table.add_row(["check vulnerabilities on TARGET", "Vuln scripts"])
    table.add_row(["discover devices on TARGET", "Network discovery"])
    table.add_row(["trace route to TARGET", "Traceroute"])
    print(table)
    print(colored("\nType 'exit' to quit\n", "cyan"))

def main():
    print(colored("\nNmapBot – Natural Language Nmap", "green"))
    print(colored("Type 'help' for examples\n", "cyan"))
    while True:
        try:
            command = input(colored("NmapBot > ", "yellow"))
        except KeyboardInterrupt:
            print("\nExiting NmapBot")
            sys.exit()
        if command.lower() == "exit": sys.exit()
        elif command.lower() == "help": help_menu()
        else: parse_command(command)

if __name__ == "__main__":
    main()
EOPY

# Make script executable
chmod +x nmapbot.py
ln -sf $(pwd)/nmapbot.py $PREFIX/bin/nmapbot

echo "Installation complete! Run with: nmapbot"
EOF

# Run the installer
bash install.sh


Once installation completes:
nmapbot
