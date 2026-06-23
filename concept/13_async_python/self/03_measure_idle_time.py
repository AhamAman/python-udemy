import time

def simulate_network_io_call():
    # Simulates the execution gap of network/disk I/O latency
    time.sleep(1.5)

def simulate_cpu_computations():
    # Simulates active CPU register utilization (e.g., token parsing or math logic)
    accumulator = 0
    for i in range(5_000_000):
        accumulator += i
    return accumulator

def profile_execution_efficiency():
    print("=== RUNNING SYSTEM LATENCY PROFILE ===")
    
    # 1. Measure Active CPU Work Phase
    cpu_start = time.process_time() # Tracks ONLY clock cycles spent inside this process space
    real_start = time.time()         # Tracks real-world clock wall time
    
    simulate_cpu_computations()
    
    cpu_duration = time.process_time() - cpu_start
    print(f"  * CPU Computing Cycles Consumed: {cpu_duration:.4f} seconds")
    
    # 2. Measure Passive Blocking I/O Phase
    io_start = time.time()
    simulate_network_io_call()
    io_waiting_duration = time.time() - io_start
    
    total_wall_time = time.time() - real_start
    
    # Calculate efficiency percentage
    efficiency_ratio = (cpu_duration / total_wall_time) * 100
    
    print(f"  * Idle Network I/O Waiting Time: {io_waiting_duration:.4f} seconds")
    print("--------------------------------------------------")
    print(f"Total Real-World Wall Clock Time:  {total_wall_time:.4f} seconds")
    print(f"Hardware Resource Efficiency:      {efficiency_ratio:.2f}%")
    print(f"System Waste Factor:               {100 - efficiency_ratio:.2f}%")

if __name__ == "__main__":
    profile_execution_efficiency()