import asyncio
import time

async def simulate_data_fetch(resource_id):
    print(f"  [Coroutine-{resource_id}] Ingest connection opened. Pausing for I/O...")
    
    # Non-blocking yield to the event loop
    await asyncio.sleep(1.5)
    
    print(f"  [Coroutine-{resource_id}] Data received from hardware buffer!")
    return f"Payload_Data_For_{resource_id}"

async def main():
    print("=== STARTING SIMPLE COROUTINE DEMO ===")
    start_time = time.time()

    # WRONG WAY: Calling it like a regular function
    incorrect_call = simulate_data_fetch("Resource-A")
    print(f"\nDirect execution token type: {type(incorrect_call)}")
    # Notice that absolutely nothing printed from inside simulate_data_fetch yet!
    
    print("\n------------------------------------------------")
    print("Activating the coroutine correctly using 'await'...\n")
    
    # RIGHT WAY: Awaiting the coroutine object inside an active loop
    # This unpacks the generator and schedules it onto the thread
    result = await incorrect_call
    
    print(f"\nReturned extraction output: '{result}'")
    print(f"Total processing wall time: {time.time() - start_time:.2f} seconds")

if __name__ == "__main__":
    # Boot the event loop engine and feed it our main coroutine entry point
    asyncio.run(main())