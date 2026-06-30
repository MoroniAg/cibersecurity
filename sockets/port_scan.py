import socket

def scan_port(host: str, port: int) -> bool:

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)

    try:
        return sock.connect_ex((host, port)) == 0
    finally:
        sock.close()

def scan_host(host: str)-> list[int]:
    open_ports = []

    for port in range(1, 1025):
        if scan_port(host, port):
            open_ports.append(port)

    return open_ports


def main():


    host = HOST
    open_ports = scan_host(host)

    print(open_ports)

if __name__ == "__main__":
    main()