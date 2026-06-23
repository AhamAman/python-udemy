import asyncio

async def command_router(reader, writer):
    client_addr = writer.get_extra_info('peername')
    print(f"[Server] Client {client_addr} connected.")
    
    # Send a welcome banner to the client upon handshake
    writer.write(b"WELCOME TO ACCELERATED ECHO ENGINE. READY FOR COMMANDS.\n")
    await writer.drain()
    
    try:
        while True:
            data = await reader.readline()
            if not data:
                break
                
            raw_msg = data.decode().strip()
            print(f"[Server Log] [{client_addr}]: {raw_msg}")
            
            # Simple Protocol Router Logic
            if raw_msg.upper() == "PING":
                response = "PONG\n"
            elif raw_msg.upper().startswith("UPPER "):
                content = raw_msg[6:] # Strip out the 'UPPER ' token prefix
                response = f"{content.upper()}\n"
            elif raw_msg.upper() == "QUIT":
                writer.write(b"GOODBYE.\n")
                await writer.drain()
                break
            else:
                response = f"ERR: UNKNOWN_COMMAND ('{raw_msg}')\n"
                
            writer.write(response.encode())
            await writer.drain()
            
    except Exception as err:
        print(f"[Server Exception] Fault isolated on {client_addr}: {err}")
    finally:
        print(f"[Server] Terminating channel connection for {client_addr}")
        writer.close()
        await writer.wait_closed()

async def main():
    server = await asyncio.start_server(command_router, '127.0.0.1', 8888)
    print("[Server] Command Echo Server listening on port 8888...")
    async with server:
        await server.serve_forever()

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\n[Server] Shutting down.")