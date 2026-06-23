import time
from concurrent.futures import ProcessPoolExecutor

def generate_sensor_telemetry_dump():
    print("Generating 10,000,000 raw numeric sensor data tokens in heap memory...")
    # Simulated temperature logs from an industrial plant grid
    return [i % 150 for i in range(10_000_000)]

def crunch_data_chunk_worker(data_chunk_slice):
    """Analyzes a large raw list chunk locally within its process memory silo"""
    anomalies_detected = 0
    # Search for temperatures over an operational threshold
    for reading in data_chunk_slice:
        if reading > 135:
            anomalies_detected += 1
    return anomalies_detected

if __name__ == "__main__":
    dataset = generate_sensor_telemetry_dump()
    print(f"Dataset compiled. Size: {len(dataset):,} entries.")
    
    start_time = time.time()
    
    # CHUNKING PARADIGM: Divide the 10 million rows into 4 distinct slices of 2.5 million each
    chunk_size = 2_500_000
    data_chunks = [dataset[i:i + chunk_size] for i in range(0, len(dataset), chunk_size)]
    
    print(f"Segmented data matrix into {len(data_chunks)} memory chunks for worker distribution.")
    
    # Process the chunks concurrently across separate processes
    with ProcessPoolExecutor(max_workers=4) as executor:
        # Distribute the chunks across the pool
        futures = [executor.submit(crunch_data_chunk_worker, chunk) for chunk in data_chunks]
        
        # Gather (Reduce Phase): Combine individual counts into a single global metric
        total_anomalies = sum(f.result() for f in futures)
        
    duration = time.time() - start_time
    
    print("\n================ SYSTEM AUDIT REPORT ================")
    print(f" Total Sensor Readings Parsed:  {len(dataset):,}")
    print(f" Critical Anomalies Identified:  {total_anomalies:,}")
    print(f" Total Multi-Process Processing Time:  {duration:.4f} seconds")