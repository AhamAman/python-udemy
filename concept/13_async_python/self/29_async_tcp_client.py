import asyncio

async def send_network_messages():
    print("=== INITIALIZING TCP CLIENT SOCKET MATRIX ===")
    
    # Establish a non-blocking TCP handshake connection with our local server
    reader, writer = await asyncio.open_connection('127.0.0.1', 8888)
    print("[Client] Handshake resolved. Socket channel fully operational.\n")
    
    messages_to_transmit = [
        "Hello from the asynchronous boundary!",
        "Query: Fetch cluster metrics payload",
        "Final close token sequence."
    ]
    
    for message in messages_to_transmit:
        print(f"[Client] Sending stream payload: '{message}'")
        # Prepend a newline char so the server's readline() knows when a frame ends
        payload = f"{message}\n".encode()
        
        writer.write(payload)
        await writer.drain() # Yield control until bytes leave the network buffer
        
        # Read the echo response coming back over the wire
        server_reply = await reader.readline()
        print(f"[Client] Response payload unpacked: '{server_reply.decode().strip()}'\n")
        
        # Pause briefly between transmissions to simulate client pacing
        await asyncio.sleep(1.0)
        
    print("[Client] Finalizing transmission. Sending closing flags...")
    writer.close()
    await writer.wait_closed()
    print("[Client] Socket connection dropped cleanly.")

if __name__ == "__main__":
    asyncio.run(send_network_messages())