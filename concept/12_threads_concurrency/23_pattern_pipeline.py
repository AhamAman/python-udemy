import threading
import queue
import time

# Channels linking pipeline components
raw_to_transform_queue = queue.Queue(maxsize=3)
transform_to_sink_queue = queue.Queue(maxsize=3)

def stage_1_ingestor(raw_strings):
    for item in raw_strings:
        print(f"[Stage 1 Ingest] Loading raw item: '{item}'")
        time.sleep(0.2) # Simulate fast intake
        raw_to_transform_queue.put(item)
    # Signal termination to Stage 2
    raw_to_transform_queue.put(None)

def stage_2_transformer():
    while True:
        item = raw_to_transform_queue.get()
        if item is None:
            raw_to_transform_queue.task_done()
            break
            
        print(f"  [Stage 2 Transform] Uppercasing: '{item}'")
        time.sleep(0.5) # Simulate moderate transform work
        transformed = item.upper()
        
        transform_to_sink_queue.put(transformed)
        raw_to_transform_queue.task_done()
    # Signal termination to Stage 3
    transform_to_sink_queue.put(None)

def stage_3_sink():
    while True:
        item = transform_to_sink_queue.get()
        if item is None:
            transform_to_sink_queue.task_done()
            break
            
        print(f"    [Stage 3 Sink] Writing to secure storage: '*** {item} ***'")
        time.sleep(0.3)
        transform_to_sink_queue.task_done()

if __name__ == "__main__":
    data_stream = ["kernel", "deadlock", "mutex", "syscall", "thread"]
    print(f"=== INITIALIZING STREAMING PIPELINE FOR {len(data_stream)} ITEMS ===\n")
    
    t1 = threading.Thread(target=stage_1_ingestor, args=(data_stream,))
    t2 = threading.Thread(target=stage_2_transformer)
    t3 = threading.Thread(target=stage_3_sink)
    
    t1.start()
    t2.start()
    t3.start()
    
    t1.join()
    t2.join()
    t3.join()
    print("\n=== PIPELINE FULLY DRAINED ===")