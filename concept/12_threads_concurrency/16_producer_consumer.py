import threading
import time
import random

BUFFER_MAX_SIZE = 3
shared_buffer = []

# Synchronization & Signaling Primitive
buffer_condition = threading.Condition()

def producer_worker(total_items):
    for i in range(total_items):
        time.sleep(random.uniform(0.2, 0.6)) # Simulate time taken to generate data
        
        with buffer_condition:
            # If the shared buffer queue is full, the producer must wait
            while len(shared_buffer) == BUFFER_MAX_SIZE:
                print("  [Buffer Full] Producer is waiting for space...")
                buffer_condition.wait() # Releases lock and blocks thread
            
            item_data = f"Data-Packet-{i}"
            shared_buffer.append(item_data)
            print(f"[PRODUCED] {item_data}. Buffer size: {len(shared_buffer)}")
            
            # Notify any sleeping consumers that new data is available
            buffer_condition.notify()

def consumer_worker(total_items):
    for _ in range(total_items):
        time.sleep(random.uniform(0.4, 0.9)) # Simulate time taken to process data
        
        with buffer_condition:
            # If the shared buffer queue is completely empty, the consumer must wait
            while len(shared_buffer) == 0:
                print("  [Buffer Empty] Consumer is waiting for data...")
                buffer_condition.wait() # Releases lock and blocks thread
            
            item_data = shared_buffer.pop(0)
            print(f"    [CONSUMED] Processed {item_data}. Buffer size: {len(shared_buffer)}")
            
            # Notify any sleeping producers that a slot has freed up
            buffer_condition.notify()

if __name__ == "__main__":
    print("=== STARTING PRODUCER-CONSUMER ORCHESTRATION ===")
    
    items_to_handle = 8
    
    producer = threading.Thread(target=producer_worker, args=(items_to_handle,))
    consumer = threading.Thread(target=consumer_worker, args=(items_to_handle,))
    
    producer.start()
    consumer.start()
    
    producer.join()
    consumer.join()
    
    print("\n=== PIPELINE PROCESSING COMPLETED ===")