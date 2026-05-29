from random import choice

tools = ["Nmap", "Wireshark", "Metasploit", "Burp Suite", "Nessus"]
tool = choice(tools)
print(f"\nToday's tool to learn:{tool}")