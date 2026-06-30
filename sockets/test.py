import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

sock.connect(("example.com", 80))

sock.close()

sock.connect(("example.com", 443))