import asyncio
import time

async def write_to_database(order_id):
    print(f"      [Low-Level DB] Writing order {order_id} to disk page storage...")
    await asyncio.sleep(1.0) # Simulating disk seek I/O latency
    print(f"      [Low-Level DB] Database commit finalized successfully.")
    return True

async def validate_payment(user_name, amount):
    print(f"    [Mid-Level Payment] Pinging banking gateway API for {user_name}...")
    await asyncio.sleep(1.0) # Simulating network roundtrip latency
    print(f"    [Mid-Level Payment] Bank approved charge of ${amount}.")
    return f"AUTH_TOKEN_{int(time.time())}"

async def process_user_order(user_name, amount, order_id):
    print(f"[High-Level Order] Processing order {order_id} for {user_name}...")
    
    # Chain 1: Wait for the payment validation layer to complete
    auth_token = await validate_payment(user_name, amount)
    print(f"[High-Level Order] Received authorization: {auth_token}")
    
    # Chain 2: Wait for the database write layer to complete
    db_status = await write_to_database(order_id)
    
    if db_status:
        print(f"[High-Level Order] Order {order_id} fully placed!")

if __name__ == "__main__":
    print("=== STARTING NESTED COROUTINE CHAIN EXECUTION ===\n")
    start_time = time.time()
    
    # Execute the top of the chain
    asyncio.run(process_user_order("Alice", 150.00, "ORD-99214"))
    
    print(f"\nOrder pipeline finalized in {time.time() - start_time:.2f} seconds total.")