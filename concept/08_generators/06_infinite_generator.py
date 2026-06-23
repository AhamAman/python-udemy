import itertools
import time

# ==========================================
# 1. Defining Infinite Data Stream Engines
# ==========================================

def infinite_fibonacci_generator():
    """Generates an unbounded Fibonacci sequence using lazy evaluation state preservation."""
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b  # The underlying state math is frozen on the heap at each yield

def continuous_telemetry_ping():
    """Simulates an infinite network heartbeat telemetry ping stream."""
    ping_count = 1
    while True:
        # Yields structured metrics payload on demand
        yield {"event_id": f"PING_{ping_count:04d}", "timestamp": time.time()}
        ping_count += 1


# ==========================================
# 2. Safe Limiting Pattern A: The Manual Break Guard
# ==========================================
print("--- 1. Consuming Infinite Streams Safely with Manual Breaks ---")

fib_stream = infinite_fibonacci_generator()

# A classic loop counter acts as a safety gatekeeper
for index, value in enumerate(fib_stream):
    print(f"  Fibonacci Sequence Pos {index}: {value}")
    
    if index >= 5:  # Strict boundary control check
        print("  -> Boundary condition reached. Manually breaking loop execution.")
        break


# ==========================================
# 3. Safe Limiting Pattern B: Functional Slicing via islice()
# ==========================================
print("\n--- 2. Stream Slicing via itertools.islice() ---")

ping_stream = continuous_telemetry_ping()

# itertools.islice wraps around the infinite generator,
# automatically raising a StopIteration exception after processing exactly 3 items.
safe_sliced_pipeline = itertools.islice(ping_stream, 3)

print("Pulling records from sliced streaming pipeline:")
for network_packet in safe_sliced_pipeline:
    print(f"  Dispatched Telemetry Log: {network_packet}")

print("-> Success: Stream pipeline severed cleanly by slicing engine.")