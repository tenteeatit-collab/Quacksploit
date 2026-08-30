#!/bin/bash
echo "[+] Installing Quacksploit..."
curl -sL https://raw.githubusercontent.com/tenteeatit-collab/Quacksploit/main/quacksploit.py -o $PREFIX/bin/quacksploit
chmod +x $PREFIX/bin/quacksploit
echo "[+] Done! Type 'quacksploit' to run."
