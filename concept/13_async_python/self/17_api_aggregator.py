import asyncio
import time

async def fetch_inventory_status():
    await asyncio.sleep(0.8) # Simulate fast database lookups
    return {"inventory": "In_Stock", "sku_count": 42}

async def fetch_user_profile():
    await asyncio.sleep(0.5) # Simulate cache fetch
    return {"user_tier": "VIP_Gold", "account_id": 99421}

async def fetch_shipping_rates_gateway():
    print("  [External Gateway] Connecting to Third-Party Shipping API...")
    await asyncio.sleep(1.5)
    # Simulating a sudden remote server gateway outage
    print("  [External Gateway] 🔴 Connection timeout on carrier server!")
    raise ConnectionError("Carrier gateway connection dropped mid-handshake.")

async def main():
    print("=== BOOTING CONCURRENT CHECKOUT AGGREGATION ENGINE ===\n")
    start_time = time.time()
    
    # Deploy all coroutines together as concurrent paths
    inventory_coro = fetch_inventory_status()
    user_coro = fetch_user_profile()
    shipping_coro = fetch_shipping_rates_gateway()
    
    print("[Main Loop] Dispatching calls concurrently to internal and external microservices...")
    
    # CRUCIAL CONFIGURATION: return_exceptions=True preserves successful data blocks
    aggregated_responses = await asyncio.gather(
        inventory_coro, 
        user_coro, 
        shipping_coro, 
        return_exceptions=True
    )
    
    print("\n================ COMPILER SUMMARY MATRIX ================")
    print(f"Aggregator pipeline returned {len(aggregated_responses)} payload tracks at {time.time() - start_time:.2f}s:\n")
    
    # Map array indices straight to clean business parameters
    inventory_data = aggregated_responses[0]
    user_data      = aggregated_responses[1]
    shipping_data  = aggregated_responses[2]
    
    # Process or handle each record safely using isinstance checks
    if not isinstance(inventory_data, Exception):
        print(f" ✅ [INVENTORY SECTOR] Status: {inventory_data['inventory']} (SKUs: {inventory_data['sku_count']})")
        
    if not isinstance(user_data, Exception):
        print(f" ✅ [ACCOUNT SECTOR] Verification: Clear | Tier: {user_data['user_tier']}")
        
    if isinstance(shipping_data, Exception):
        # Trace fallback mitigation patterns
        print(f" ⚠️  [SHIPPING SECTOR ALERT] Graceful Degradation Triggered!")
        print(f"    -> Root Cause: Caught Exception -> '{shipping_data}'")
        print(f"    -> Countermeasure: Falling back to flat-rate baseline shipping ($5.00).")

if __name__ == "__main__":
    asyncio.run(main())