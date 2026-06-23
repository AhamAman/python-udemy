import asyncio

# Shared memory infrastructure tracking active stream nodes
# Single-threaded execution means no race conditions on set modifications
connected_clients = set()

async def broadcast_to_all_peers(sender_address, message_text):
    """Iterates through the channel registry matrix and flushes out bytes."""
    outbound_payload = f"[{sender_address[1]}]: {message_text}\n".encode()
    
    # Collect all closed references to prune them after iteration
    dead_connections = set()
    
    for client_writer in connected_clients:
        # Avoid echoing the message back to the original author
        if client_writer.get_extra_info('peername') != sender_address:
            try:
                client_writer.write(outbound_payload)
                # Note: We track draining sequentially inside this loop context
                await client_writer.drain()
            except Exception:
                dead_connections.add(client_writer)
                
    # Keep the global set clean of memory leaks
    if dead_connections:
        connected_clients.difference_update(dead_connections)

async def chat_handler(reader, writer):
    client_address = writer.get_extra_info('peername')
    print(f"[Chat Room] 🟢 User entered grid from port: {client_address}")
    
    # Register client writer frame into global broker matrix
    connected_clients.add(writer)
    
    writer.write(b"CONNECTED TO ASYNC GLOBAL MATRIX CHAT ROOM.\n")
    await writer.drain()
    
    await broadcast_to_all_peers(client_address, "has joined the communication channel.")
    
    try:
        while True:
            data = await reader.readline()
            if not data:
                break
                
            incoming_text = data.decode().strip()
            if incoming_text:
                print(f"[Room Log] Broadcast from {client_address}: '{incoming_text}'")
                await broadcast_to_all_peers(client_address, incoming_text)
                
    except Exception as err:
        print(f"[Room Log] Error on socket path {client_address}: {err}")
    finally:
        print(f"[Chat Room] 🔴 User disconnected from port: {client_address}")
        connected_clients.discard(writer)
        writer.close()
        await writer.wait_closed()
        await broadcast_to_all_peers(client_address, "has left the channel layout.")

async def main():
    server = await asyncio.start_server(chat_handler, '127.0.0.1', 9999)
    print("🚀 Chat Matrix Server active and spinning on port 9999...")
    async with server:
        await server.serve_forever()

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\n[Chat Room] Server infrastructure offline.")