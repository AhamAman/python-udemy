import asyncio
import time

async def low_level_hardware_io():
    print("      [Layer-3] [Low-Level IO] Pinging physical network interface card...")
    # This is the actual system boundary suspension point
    await asyncio.sleep(1.5)
    print("      [Layer-3] [Low-Level IO] Hard hardware response bytes captured!")
    return {"status_code": 200, "payload": "Database-Record-X"}

async def mid_level_data_parser():
    print("    [Layer-2] [Mid-Level Parser] Invoking lower hardware interface layer...")
    # Awaits low level: Layer 2 suspends until Layer 3 returns data
    raw_response = await low_level_hardware_io()
    
    print("    [Layer-2] [Mid-Level Parser] Unpacking raw bytes into memory schema...")
    return f"Parsed_Object({raw_response['payload']})"

async def high_level_application_router():
    print("[Layer-1] [High-Level Router] Request received. Routing to parsing engine...")
    # Awaits mid level: Layer 1 suspends until Layer 2 returns data
    final_model = await mid_level_data_parser()
    
    print(f"[Layer-1] [High-Level Router] Rendering user response frame: {final_model}")

if __name__ == "__main__":
    print("=== BOOTING NESTED CALL STACK SIMULATION ===\n")
    start = time.time()
    
    asyncio.run(high_level_application_router())
    
    print(f"\nNested structural lifecycle resolved in {time.time() - start:.2f} seconds.")