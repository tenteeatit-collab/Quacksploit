#!/usr/bin/env python3
import os, sys, json
from datetime import datetime

DATA_DIR = os.path.expanduser("~/quacksploit_data")
EXPLOIT_DB = os.path.join(DATA_DIR, "exploits.json")

GREEN = "\033[92m"; RED = "\033[91m"; YELLOW = "\033[93m"; CYAN = "\033[96m"; RESET = "\033[0m"; BOLD = "\033[1m"

def banner():
    os.system('clear')
    print(f"""{CYAN}
    ╔═══════════════════════════════════════════╗
    ║  {BOLD}QUACKSPLOIT - Exploit Database{RESET}{CYAN}      ║
    ║  {YELLOW}🦆 Cyber Security Framework{RESET}{CYAN}        ║
    ╚═══════════════════════════════════════════╝{RESET}
    """)

def init_data():
    if not os.path.exists(DATA_DIR): os.makedirs(DATA_DIR)
    if not os.path.exists(EXPLOIT_DB):
        sample = {"exploits": [
            {"id":"CVE-2024-1234","name":"Android Kernel Exploit","type":"Local","severity":"Critical","platform":"Android","description":"Privilege escalation to root","date":"2024-01-15","source":"https://example.com","status":"Active"},
            {"id":"CVE-2023-5678","name":"WebRTC Memory Corruption","type":"Remote","severity":"High","platform":"Linux","description":"Remote code execution","date":"2023-11-20","source":"https://example.com","status":"Active"},
            {"id":"CVE-2024-9012","name":"MySQL SQL Injection","type":"Remote","severity":"Medium","platform":"Linux","description":"SQL injection vulnerability","date":"2024-02-01","source":"https://example.com","status":"Patched"}
        ]}
        with open(EXPLOIT_DB, 'w') as f: json.dump(sample, f, indent=4)
        print(f"{GREEN}[+] Database created{RESET}")

def load_exploits():
    try:
        with open(EXPLOIT_DB) as f: return json.load(f).get('exploits', [])
    except: return []

def save_exploits(e):
    with open(EXPLOIT_DB, 'w') as f: json.dump({"exploits": e}, f, indent=4)

def list_exploits(e):
    if not e: print(f"{RED}[!] No exploits{RESET}"); return
    print(f"\n{BOLD}{CYAN}[+] Exploit List{RESET}\n")
    print(f"{'ID':<18} {'Name':<30} {'Severity':<12} {'Status':<10}")
    print("-"*75)
    for x in e:
        c = RED if x.get('severity') in ['Critical','High'] else YELLOW if x.get('severity')=='Medium' else GREEN
        print(f"{x.get('id',''):<18} {x.get('name','')[:28]:<30} {c}{x.get('severity',''):<12}{RESET} {x.get('status',''):<10}")
    print()

def main():
    init_data()
    exploits = load_exploits()
    while True:
        banner()
        print("[1] List exploits")
        print("[2] Search")
        print("[3] View details")
        print("[4] Add exploit")
        print("[5] Delete exploit")
        print("[6] Export HTML")
        print("[0] Exit")
        c = input(f"{YELLOW}[?] Choice: {RESET}")
        if c == '1':
            list_exploits(exploits)
            input("Press Enter...")
        elif c == '2':
            k = input("Keyword: ")
            r = [x for x in exploits if k.lower() in str(x).lower()]
            list_exploits(r) if r else print(f"{RED}[!] Not found{RESET}")
            input("Press Enter...")
        elif c == '3':
            i = input("ID: ")
            f = [x for x in exploits if x.get('id') == i]
            if f:
                x = f[0]
                print(f"\n{BOLD}ID:{RESET} {x.get('id')}")
                print(f"{BOLD}Name:{RESET} {x.get('name')}")
                print(f"{BOLD}Type:{RESET} {x.get('type')}")
                print(f"{BOLD}Severity:{RESET} {x.get('severity')}")
                print(f"{BOLD}Platform:{RESET} {x.get('platform')}")
                print(f"{BOLD}Description:{RESET} {x.get('description')}")
                print(f"{BOLD}Source:{RESET} {x.get('source')}")
            else:
                print(f"{RED}[!] Not found{RESET}")
            input("Press Enter...")
        elif c == '4':
            n = {}
            n['id'] = input("ID: ")
            n['name'] = input("Name: ")
            n['type'] = input("Type (Local/Remote/Network): ")
            n['severity'] = input("Severity (Low/Medium/High/Critical): ")
            n['platform'] = input("Platform: ")
            n['description'] = input("Description: ")
            n['date'] = datetime.now().strftime("%Y-%m-%d")
            n['source'] = input("Source URL: ")
            n['status'] = input("Status (Active/Patched): ")
            exploits.append(n)
            save_exploits(exploits)
            print(f"{GREEN}[+] Added!{RESET}")
            input("Press Enter...")
        elif c == '5':
            i = input("ID to delete: ")
            for idx, x in enumerate(exploits):
                if x.get('id') == i:
                    del exploits[idx]
                    save_exploits(exploits)
                    print(f"{GREEN}[+] Deleted!{RESET}")
                    break
            else:
                print(f"{RED}[!] Not found{RESET}")
            input("Press Enter...")
        elif c == '6':
            f = f"quacksploit_{datetime.now().strftime('%Y%m%d')}.html"
            p = os.path.join(DATA_DIR, f)
            with open(p, 'w') as h:
                h.write("<html><head><title>Quacksploit</title></head><body><h1>🦆 Quacksploit</h1><table border=1>")
                h.write("<tr><th>ID</th><th>Name</th><th>Severity</th><th>Status</th></tr>")
                for x in exploits:
                    h.write(f"<tr><td>{x.get('id')}</td><td>{x.get('name')}</td><td>{x.get('severity')}</td><td>{x.get('status')}</td></tr>")
                h.write("</table></body></html>")
            print(f"{GREEN}[+] Exported: {p}{RESET}")
            input("Press Enter...")
        elif c == '0':
            print(f"{CYAN}🦆 Bye!{RESET}")
            sys.exit(0)
        else:
            print(f"{RED}[!] Invalid{RESET}")
            input("Press Enter...")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n{CYAN}🦆 Exiting...{RESET}")
        sys.exit(0)
