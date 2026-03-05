# RobotScan Pro

RobotScan Pro is a **natural language interface for Nmap**, designed for Termux and Linux.  
Users can type human-readable sentences to perform advanced network scanning without remembering Nmap flags.

---

## Installation

```bash
git clone https://github.com/YourUsername/RobotScanPro.git
cd RobotScanPro
bash install.sh

> Replace YourUsername with your GitHub username.




---

Launch RobotScan Pro

robotscan

You will see:

RobotScan Pro – Natural Language Nmap
Type 'help' for examples
Robot >


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
check vulnerabilities on TARGET	Run NSE vulnerability scripts
discover devices on TARGET	Network discovery / ping sweep
trace route to TARGET	Traceroute
help	Show all commands
exit	Quit RobotScan Pro



---

Example Usage

robotscan
check open ports on scanme.nmap.org
run stealth scan on example.com
scan example.com for services
find operating system of example.com
check vulnerabilities on example.com
discover devices on 192.168.1.0/24
trace route to example.com
run aggressive scan on example.com
exit

> Replace TARGET with a domain name, IP address, or subnet.




---

Folder Structure

RobotScanPro/
├─ robotscan.py          # main CLI script
├─ install.sh            # installer
├─ reports/              # scan results (auto-saved)
├─ profiles/             # optional scan profiles
├─ scripts/              # optional NSE scripts
├─ README.md             # this file
└─ requirements.txt      # python dependencies


---

Requirements

Python 3

Nmap

Termux or Linux terminal

Python libraries: colorama, termcolor, prettytable



---

Tips

Use one sentence per scan for clarity.

All scans automatically save results in reports/ folder.

Type help to see the full list of natural language commands.

Type exit to quit RobotScan Pro.



---

License

MIT License – free to use and modify.
