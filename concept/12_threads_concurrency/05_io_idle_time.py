import time
import os
import requests

def run_demo():
    print("==================================================")
    print("      STARTING DISK & NETWORK IDLE TELEMETRY       ")
    print("==================================================")

    # ----------------------------------------------------
    # PHASE 1: Sequential File Processing (Disk I/O)
    # ----------------------------------------------------
    print("\n[Phase 1] Executing Sequential File Processing...")
    
    disk_start_wall = time.time()
    disk_start_cpu = time.process_time()
    
    # Simulating heavy sequential file operations
    filenames = [f"temp_test_file_{i}.txt" for i in range(50)]
    
    # Sequentially write files
    for name in filenames:
        with open(name, "w") as f:
            f.write("Some dummy data to force disk allocation\n" * 5000)
            
    # Sequentially read files back
    for name in filenames:
        with open(name, "r") as f:
            _ = f.read()
            
    # Cleanup files
    for name in filenames:
        os.remove(name)
        
    disk_end_wall = time.time()
    disk_end_cpu = time.process_time()
    
    disk_wall_elapsed = disk_end_wall - disk_start_wall
    disk_cpu_elapsed = disk_end_cpu - disk_start_cpu
    disk_idle = disk_wall_elapsed - disk_cpu_elapsed

    # ----------------------------------------------------
    # PHASE 2: Sequential Network Requests (Network I/O)
    # ----------------------------------------------------
    print("\n[Phase 2] Executing Sequential Network Requests...")
    
    net_start_wall = time.time()
    net_start_cpu = time.process_time()
    
    # We will make 3 real-world HTTP requests sequentially
    urls = [
        "https://httpbin.org/delay/1",
        "https://httpbin.org/delay/1",
        "https://httpbin.org/delay/1"
    ]
    
    for i, url in enumerate(urls, 1):
        print(f"  -> Requesting API endpoint {i}/3...")
        response = requests.get(url)
        _ = response.text # Consume payload
        
    net_end_wall = time.time()
    net_end_cpu = time.process_time()
    
    net_wall_elapsed = net_end_wall - net_start_wall
    net_cpu_elapsed = net_end_cpu - net_start_cpu
    net_idle = net_wall_elapsed - net_cpu_elapsed

    # ----------------------------------------------------
    # TELEMETRY DASHBOARD
    # ----------------------------------------------------
    print("\n==================================================")
    print("                FINAL TELEMETRY REPORT            ")
    print("==================================================")
    
    print(f"DISK I/O (Sequential Files):")
    print(f"  Real-World Time:  {disk_wall_elapsed:.4f} seconds")
    print(f"  CPU Work Time:    {disk_cpu_elapsed:.4f} seconds")
    print(f"  Wasted Idle Time: {disk_idle:.4f} seconds")
    print(f"  CPU Efficiency:   {(disk_cpu_elapsed / disk_wall_elapsed) * 100:.2f}%")
    
    print(f"\nNETWORK I/O (Sequential Requests):")
    print(f"  Real-World Time:  {net_wall_elapsed:.4f} seconds")
    print(f"  CPU Work Time:    {net_cpu_elapsed:.4f} seconds")
    print(f"  Wasted Idle Time: {net_idle:.4f} seconds")
    print(f"  CPU Efficiency:   {(net_cpu_elapsed / net_wall_elapsed) * 100:.2f}%")

if __name__ == "__main__":
    run_demo()