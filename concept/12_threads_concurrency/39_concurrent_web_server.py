import socket
import threading
import time

def handle_client_connection(client_socket, client_address, request_id):
    print(f"  [Thread-{request_id}] Handle connection started for {client_address}")
    
    try:
        # 1. Read the inbound raw HTTP request payload bytes from the socket
        request_data = client_socket.recv(1024).decode('utf-8')
        
        # Extract the first line of the HTTP request to see the path
        if request_data:
            first_line = request_data.split('\n')[0]
            print(f"  [Thread-{request_id}] Received: {first_line.strip()}")
            
        # 2. Simulate slow business logic (e.g., intensive I/O database lookup)
        # This forces the thread into a WAITING state, but leaves the server core free
        time.sleep(3)
        
        # 3. Construct a standard raw HTTP text response frame
        http_response = (
            "HTTP/1.1 200 OK\r\n"
            "Content-Type: text/plain\r\n"
            "Connection: close\r\n"
            "\r\n"
            f"Hello World! Your request was processed concurrently by Thread-{request_id}.\n"
        )
        
        # 4. Push the bytes out through the network interface socket card
        client_socket.sendall(http_response.encode('utf-8'))
        
    except Exception as e:
        print(f"  [Thread-{request_id}] Error handling request: {e}")
    finally:
        # 5. Clean up and close the network file descriptor resource
        client_socket.close()
        print(f"  [Thread-{request_id}] Connection with {client_address} closed cleanly.")

def run_concurrent_server():
    # Create an IPv4 (AF_INET), streaming TCP (SOCK_STREAM) network socket primitive
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Allow instant re-binding to this port if the server restarts
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    
    server_host = '127.0.0.1'
    server_port = 8080
    server_socket.bind((server_host, server_port))
    
    # Enable the OS kernel network buffer queue to listen for incoming handshakes
    server_socket.listen(128)
    
    print(f"=== CONCURRENT TCP WEB SERVER LISTENING ON http://{server_host}:{server_port} ===")
    print("Open multiple browser tabs or use curl to test simultaneous hits...\n")
    
    request_counter = 0
    
    try:
        while True:
            # accept() blocks the main thread until a new TCP handshake completes
            client_sock, client_addr = server_socket.accept()
            request_counter += 1
            
            print(f"\n[Main Dispatcher] Accepted connection #{request_counter} from {client_addr}")
            
            # THE THREAD-PER-REQUEST PATTERN
            # Instead of processing the socket sequentially here, we wrap the socket 
            # and hand it off to a completely isolated background worker thread
            worker_thread = threading.Thread(
                target=handle_client_connection,
                args=(client_sock, client_addr, request_counter),
                name=f"RequestWorker-{request_counter}"
            )
            
            # Spin up the background thread. The main loop returns to accept() instantly!
            worker_thread.start()
            
    except KeyboardInterrupt:
        print("\nShutting down network server matrix.")
    finally:
        server_socket.close()

if __name__ == "__main__":
    run_concurrent_server()