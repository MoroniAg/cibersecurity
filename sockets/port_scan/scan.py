import json
import socket
import time

from concurrent.futures import ThreadPoolExecutor

from config import (
    TIMEOUT,
    START_PORT,
    END_PORT,
    MAX_WORKERS,
    OUTPUT_FILE
)


def resolve_host(host: str) -> str:
    return socket.gethostbyname(host)


def scan_port(host: str, port: int):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(TIMEOUT)
    try:
        opened = sock.connect_ex((host, port)) == 0
        return port, opened
    finally:
        sock.close()


def scan_host(host: str) -> list:
    open_ports = []
    with ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
        futures = []
        for port in range(START_PORT, END_PORT + 1):
            futures.append(
                executor.submit(
                    scan_port,
                    host,
                    port
                )
            )
        for future in futures:
            port, opened = future.result()
            if opened:
                open_ports.append(port)
    return open_ports


def grab_banner(host: str, port: int):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(TIMEOUT)
    try:
        sock.connect((host, port))
        banner = sock.recv(1024)
        if not banner:
            return None
        return banner.decode(errors="ignore").strip()
    except Exception:
        return None
    finally:
        sock.close()


def save_json(host, ip, results):
    data = {
        "host": host,
        "ip": ip,
        "results": results
    }
    with open(OUTPUT_FILE, "w") as file:
        json.dump(
            data,
            file,
            indent=4
        )


def run(host: str):
    start = time.perf_counter()
    ip = resolve_host(host)
    open_ports = scan_host(ip)
    results = []
    for port in open_ports:
        banner = grab_banner(ip, port)
        results.append(
            {
                "port": port,
                "banner": banner
            }
        )
    elapsed = time.perf_counter() - start
    save_json(
        host,
        ip,
        results
    )
    return ip, results, elapsed
