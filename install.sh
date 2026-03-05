#!/bin/bash
echo "Installing NmapBot..."

pkg update -y && pkg upgrade -y
pkg install python nmap git wget -y
pip install colorama prettytable termcolor

chmod +x nmapbot.py
ln -sf $(pwd)/nmapbot.py $PREFIX/bin/nmapbot

echo "Installation complete! Run with: nmapbot"
