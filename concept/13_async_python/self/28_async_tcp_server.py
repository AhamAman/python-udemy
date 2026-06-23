import asyncio

async def handle_client_connection(reader, writer):
    """
    Spawns concurrently for every individual TCP client socket that connects.
    """
    client_address = writer.get_extra_info('peername')
    print(f"\n[Server] 🔌 New connection accepted from client node: {client_address}")
    
    try:
        while True:
            # SUSPENSION POINT: Yields control until bytes arrive on this specific socket
            data_bytes = await reader.readline()
            
            if not data_bytes:
                # An empty byte payload indicates the client closed their connection
                print(f"[Server] Client {client_address} disconnected cleanly.")
                break
                
            incoming_message = data_bytes.decode().strip()
            print(f"[Server] [Received from {client_address}]: '{incoming_message}'")
            
            # Echo the processed string back to the client
            outbound_response = f"SERVER_ECHO: {incoming_message}\n".encode()
            writer.write(outbound_response)
            
            # SUSPENSION POINT: Flushes internal buffers and yields until network pipe clears
            await writer.drain()
            
    except Exception as err:
        print(f"[Server] 💥 Connection error occurred with client {client_address}: {err}")
    finally:
        print(f"[Server] Closing connection channel for {client_address}")
        writer.close()
        await writer.wait_closed()

async def main():
    print("=== INITIALIZING CONCURRENT ASYNCIO TCP SERVER ===")
    
    # Start the network listener on local port 8888
    # Under the hood, this sets the socket to non-blocking and handles connection multiplexing
    server = await asyncio.start_server(handle_client_connection, '127.0.0.1', 8888)
    
    server_addresses = [sock.getsockname() for sock in server.sockets]
    print(f"[Server] Listening on socket array boundaries: {server_addresses}")
    print("[Server] Ready to accept remote traffic. Press Ctrl+C to terminate.\n")
    
    # Run the server loop indefinitely
    async with server:
        await server.serve_forever()

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\n[Server] Core matrix shutdown executed cleanly.")