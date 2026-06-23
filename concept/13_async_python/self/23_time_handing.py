import asyncio
import time

async def unstable_payment_gateway():
    print("  [Gateway] Handshaking with overseas banking endpoint...")
    # Simulating a stalled gateway connection that takes 5 seconds to respond
    await asyncio.sleep(5.0)
    print("  [Gateway] Transaction success packet generated.")
    return "SUCCESS_TOKEN_9912"

async def main():
    print("=== INITIALIZING PAYMENT GATEWAY SENTINEL ===")
    start_time = time.time()
    
    # We allocate a strict 1.5-second budget for this transaction
    timeout_budget = 1.5
    print(f"[Main] Dispatching transaction. Policy: Timeout after {timeout_budget}s.")
    
    try:
        # wait_for creates an atomic timeout envelope around the coroutine
        secure_token = await asyncio.wait_for(unstable_payment_gateway(), timeout=timeout_budget)
        print(f"[Main] Payment approved! Token: {secure_token}")
        
    except asyncio.TimeoutError:
        print(f"\n🚨 [TIMEOUT ENFORCED] Gateway exceeded budget limit of {timeout_budget}s!")
        print("   -> Action: Cancelled connection socket to avoid double-charging the user.")
        
    print(f"\nExecution loop finalized in {time.time() - start_time:.2f} seconds.")

if __name__ == "__main__":
    asyncio.run(main())