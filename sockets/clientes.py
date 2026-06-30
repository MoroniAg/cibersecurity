import socket
from concurrent.futures import ThreadPoolExecutor

host = "example.com"

def scan(port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)

    try:
        if sock.connect_ex((host, port)) == 0:
            print(f"[+] {port} ABIERTO")
    finally:
        sock.close()


with ThreadPoolExecutor(max_workers=1000) as executor:
    for port in range(1, 1025):
        executor.submit(scan, port)