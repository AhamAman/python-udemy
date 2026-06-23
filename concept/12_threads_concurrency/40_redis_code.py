import socket
import threading
import collections
import time

class RedisQueueServer:
    def __init__(self, host='127.0.0.1', port=6379):
        self.host = host
        self.port = port
        # In-memory database mapping keys to deques (lists)
        self.db = collections.defaultdict(collections.deque)
        # Lock to ensure atomic list manipulations across network connection threads
        self.lock = threading.Lock()
        
    def handle_client(self, client_socket):
        try:
            while True:
                # Receive raw text command from the network socket
                data = client_socket.recv(1024).decode('utf-8').strip()
                if not data:
                    break
                
                parts = data.split()
                command = parts[0].upper()
                
                if command == "LPUSH":
                    # Syntax: LPUSH queue_name task_payload
                    queue_name = parts[1]
                    payload = " ".join(parts[2:])
                    
                    with self.lock:
                        self.db[queue_name].appendleft(payload)
                        current_size = len(self.db[queue_name])
                        
                    client_socket.sendall(f"(integer) {current_size}\r\n".encode('utf-8'))
                    
                elif command == "BRPOP":
                    # Syntax: BRPOP queue_name
                    queue_name = parts[1]
                    
                    # Passive network blocking strategy
                    while True:
                        with self.lock:
                            if self.db[queue_name]:
                                item = self.db[queue_name].pop()
                                client_socket.sendall(f"{item}\r\n".encode('utf-8'))
                                break
                        # If queue is empty, block the connection thread slightly before checking again
                        time.sleep(0.1)
                else:
                    client_socket.sendall("-ERR unknown command\r\n".encode('utf-8'))
        except Exception:
            pass
        finally:
            client_socket.close()

    def start(self):
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server.bind((self.host, self.port))
        server.listen(5)
        print(f"=== IN-MEMORY REDIS-LIKE SERVER RUNNING ON {self.host}:{self.port} ===")
        
        try:
            while True:
                client_sock, addr = server.accept()
                # Handle each network client connection on a concurrent thread
                t = threading.Thread(target=self.handle_client, args=(client_sock,))
                t.daemon = True
                t.start()
        except KeyboardInterrupt:
            print("\nShutting down memory server.")
        finally:
            server.close()

if __name__ == "__main__":
    RedisQueueServer().start()