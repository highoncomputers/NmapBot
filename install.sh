#!/bin/bash
echo "Installing RobotScan Pro..."

pkg update -y && pkg upgrade -y
pkg install python nmap git wget -y
pip install colorama prettytable termcolor

chmod +x robotscan.py
ln -sf $(pwd)/robotscan.py $PREFIX/bin/robotscan

echo "Installation complete! Run with: robotscan"
