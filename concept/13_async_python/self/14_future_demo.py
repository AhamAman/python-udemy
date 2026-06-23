import asyncio

async def consumer_coroutine(name, shared_future):
    print(f"  [{name}] Consumer booted. Invoking 'await shared_future' checkpoint...")
    
    # This await point forces the consumer to freeze on the heap.
    # It will sit in the loop's Waiting Queue until someone populates the future container.
    result_payload = await shared_future
    
    print(f"  [{name}] Woke up! Extracted data from the Future box: '{result_payload}'")


async def manual_future_orchestrator():
    print("=== STARTING RAW FUTURE STATE MACHINE DEMO ===\n")

    # 1. INITIAL PENDING STATE
    # Create a raw, unpopulated Future abstraction box
    raw_future_receipt = asyncio.Future()
    
    print(f"[Main] Created Future Object instance: {raw_future_receipt}")
    print(f"   -> Initial State Validation: done() = {raw_future_receipt.done()}") # Expected: False

    # Spawn two independent consumer coroutines and pass them references to our empty future box
    consumer_1 = asyncio.create_task(consumer_coroutine("Consumer-Alpha", raw_future_receipt))
    consumer_2 = asyncio.create_task(consumer_coroutine("Consumer-Beta", raw_future_receipt))

    # Give the consumers a quick moment to run up to their active 'await shared_future' yield points
    await asyncio.sleep(0.5)
    
    print(f"\n[Main] Current Future State: done() = {raw_future_receipt.done()}")
    print("[Main] Simulating background physical I/O processing delay (2 seconds)...")
    await asyncio.sleep(2.0)

    # 2. THE COMPLETED STATE RESOLUTION
    print("\n[Main] Network bytes have hit the wire! Fulfilling the Future contract...")
    
    # Manually populate the result slot inside the Future box
    # This execution step fires a signal back to the Event Loop scheduler
    raw_future_receipt.set_result("📦 4K_Video_Asset_Stream_Bytes")
    
    print(f"   -> Updated State Validation: done() = {raw_future_receipt.done()}") # Expected: True

    # Give the loop a split second to process the wakeup transitions for the suspended consumers
    await asyncio.sleep(0.1)
    print("\n=== SYSTEM EXECUTION LIFECYCLE FINALIZED ===")

if __name__ == "__main__":
    asyncio.run(manual_future_orchestrator())