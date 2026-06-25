import socket

host = "example.com"
TIMEOUT_SECONDS = 5  # Maximum connection timeout (seconds)

# Scan ports from 70 to 80
for port in range(70, 81):
    print(f"\n--- Probing port {port} ---")
    
    try:
                # Create TCP socket for each port with configured timeout
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
                # Configure connection timeout (maximum 5 seconds)
        sock.settimeout(TIMEOUT_SECONDS)
        
        result = sock.connect_ex((host, port))  # Connection return code
        
        if result == 0:
            print(f"Port {port} open!")
            
            try:
                                # Send HTTP GET request to verify response with timeout
                request = b"GET / HTTP/1.1\r\nHost: example.com\r\nConnection: close\r\n\r\n"
                
                sock.send(request)  # Timeout included in settimeout()
                data = sock.recv(4096, TIMEOUT_SECONDS)  # Receive with timeout
                
                if len(data) > 0:
                    print(f"Response received ({len(data)} bytes):")
                    response_preview = str(data[:200]).replace('\n', '\n    ')
                    print(response_preview.rstrip())
                else:
                    print("No data received (server may be closing connection)")
            except socket.timeout as e:
                print(f"Timeout receiving response on port {port}")
        else:
            # Port closed or inaccessible
            print(f"Port {port} is not open")
            
    except Exception as e:
        print(f"Error connecting to port {port}: {e}")
    
    finally:
        sock.close()

print("\n--- Scan completed ---")
