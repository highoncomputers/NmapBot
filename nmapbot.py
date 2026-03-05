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
