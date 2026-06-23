import threading
import queue
import time
import random

def supplier_scout_worker(supplier_name, item_id, gather_queue):
    print(f"  [Scatter] {supplier_name} scout thread launched for item {item_id}...")
    
    # Simulate varying network latencies of querying different supplier databases
    query_time = random.uniform(0.5, 1.8)
    time.sleep(query_time)
    
    # Generate a mock price payload
    price = round(random.uniform(20.0, 50.0), 2)
    
    # Gather: Push results into the thread-safe communication queue as a structured tuple
    result_payload = {"supplier": supplier_name, "price": price, "latency": query_time}
    gather_queue.put(result_payload)
    print(f"  [Gathered] {supplier_name} returned price: ${price} in {query_time:.2f}s")

def run_scatter_gather_pipeline(target_item):
    print(f"=== Initiating Scatter-Gather for Item: {target_item} ===")
    start_time = time.time()
    
    suppliers = ["Supplier-US", "Supplier-EU", "Supplier-ASIA"]
    gather_queue = queue.Queue()
    threads = []
    
    # 1. THE SCATTER PHASE: Launch separate concurrent worker threads to fetch data
    for supplier in suppliers:
        t = threading.Thread(
            target=supplier_scout_worker, 
            args=(supplier, target_item, gather_queue)
        )
        threads.append(t)
        t.start()
        
    # Synchronize: Wait for all scout threads to finish their work
    for t in threads:
        t.join()
        
    # 2. THE GATHER PHASE: Collect all collected data from our communication queue
    print("\n[Main Coordinator] Consolidating collected market intelligence data...")
    final_report = []
    
    while not gather_queue.empty():
        final_report.append(gather_queue.get())
        
    # Process the gathered results
    print("\n================ FINAL REPORT ================")
    for record in final_report:
        print(f" * {record['supplier']}: ${record['price']} (Latency: {record['latency']:.2f}s)")
        
    cheapest = min(final_report, key=lambda x: x['price'])
    print("----------------------------------------------")
    print(f"RECOMMENDED BUY: {cheapest['supplier']} at ${cheapest['price']}")
    print(f"Total Aggregation Lifecycle Time: {time.time() - start_time:.2f} seconds")

if __name__ == "__main__":
    run_scatter_gather_pipeline(target_item="PRO-GPU-X100")