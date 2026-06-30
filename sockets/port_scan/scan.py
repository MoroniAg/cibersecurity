import socket
from concurrent.futures import ThreadPoolExecutor

from config import TIMEOUT, HOST, THREAD_LIMIT, PORT_START, PORT_END


def scan_port(host: str, port: int):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(TIMEOUT)
    try:
        return port, sock.connect_ex((host, port)) == 0
    finally:
        sock.close()


def scan_host(host):
    open_ports = []
    with ThreadPoolExecutor(THREAD_LIMIT) as executor:
        futures = []
        for port in range(PORT_START, PORT_END + 1):
            future = executor.submit(
                scan_port,
                host,
                port
            )
            futures.append(future)
        for future in futures:
            port, opened = future.result()
            if opened:
                open_ports.append(port)
    return open_ports
