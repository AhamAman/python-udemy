def stream_large_log_file(file_path: str):
    """Simulates streaming a multi-gigabyte production system log line-by-line."""
    # In production, use: with open(file_path, mode='r', encoding='utf-8') as file:
    # This mock simulates file object line iteration
    mock_log_lines = [
        "2026-06-23 10:00:01 STATUS=200 MSG=Healthcheck clear",
        "2026-06-23 10:01:45 STATUS=500 MSG=Database connection timeout",
        "2026-06-23 10:02:12 STATUS=200 MSG=Cache primed",
        "2026-06-23 10:05:30 STATUS=503 MSG=Service unavailable cluster_01"
    ]
    for line in mock_log_lines:
        yield line  # Suspends execution, keeping only one line in memory at a time

# 1. Instantiate the base file ingestion stream
raw_line_stream = stream_large_log_file("system.log")

# 2. Chain a lazy generator expression to filter for anomalies (5xx Errors)
anomaly_pipeline = (line for line in raw_line_stream if "STATUS=5" in line)

# 3. Chain a transformation layer to isolate the message field
final_alert_pipeline = (line.split("MSG=")[1] for line in anomaly_pipeline)

print("--- Log Processing Pipeline Results ---")
for alert in final_alert_pipeline:
    print(f"Dispatched Critical Alert Notification: {alert}")


def stream_large_log_file(file_path: str):
    """Simulates streaming a multi-gigabyte production system log line-by-line."""
    # In production, use: with open(file_path, mode='r', encoding='utf-8') as file:
    # This mock simulates file object line iteration
    mock_log_lines = [
        "2026-06-23 10:00:01 STATUS=200 MSG=Healthcheck clear",
        "2026-06-23 10:01:45 STATUS=500 MSG=Database connection timeout",
        "2026-06-23 10:02:12 STATUS=200 MSG=Cache primed",
        "2026-06-23 10:05:30 STATUS=503 MSG=Service unavailable cluster_01"
    ]
    for line in mock_log_lines:
        yield line  # Suspends execution, keeping only one line in memory at a time

# 1. Instantiate the base file ingestion stream
raw_line_stream = stream_large_log_file("system.log")

# 2. Chain a lazy generator expression to filter for anomalies (5xx Errors)
anomaly_pipeline = (line for line in raw_line_stream if "STATUS=5" in line)

# 3. Chain a transformation layer to isolate the message field
final_alert_pipeline = (line.split("MSG=")[1] for line in anomaly_pipeline)

print("--- Log Processing Pipeline Results ---")
for alert in final_alert_pipeline:
    print(f"Dispatched Critical Alert Notification: {alert}")


import time

def paginated_api_fetcher():
    """Simulates fetching items from a REST API endpoint that returns data in pages."""
    current_page = 1
    total_pages = 3
    
    while current_page <= total_pages:
        print(f"\n  [API-CLIENT] HTTP GET /v1/records?page={current_page} requested...")
        # Simulating network latency
        time.sleep(0.1) 
        
        # Mock payload response for the current page
        mock_api_page_response = [f"Record_ID_{i:03d}" for i in range((current_page-1)*3 + 1, current_page*3 + 1)]
        
        # Unroll the page batch single-file out to the consumer pipeline
        for record in mock_api_page_response:
            yield record
            
        current_page += 1

# The consumer loop treats the paginated resource as a single continuous stream
print("\n--- Paginated API Stream Processing ---")
data_feed = paginated_api_fetcher()

for index, item in enumerate(data_feed, start=1):
    print(f"    Processed Record #{index}: {item}")
    if index >= 5:
        print("    -> Consumer threshold hit. Stopping stream digestion.")
        break


import random

def live_hardware_sensor_stream():
    """Generates an infinite stream of hardware temperature telemetry sensor metrics."""
    reading_id = 1
    # Simulating a continuous hardware monitoring loop
    while reading_id <= 5:
        # Generates simulated temperature values in Celsius
        temperature_reading = round(random.uniform(20.0, 95.0), 2)
        yield {"id": reading_id, "celsius": temperature_reading}
        reading_id += 1

# 1. Boot the live sensor reader engine
sensor_feed = live_hardware_sensor_stream()

# 2. Chain a lazy transformation layout calculating Fahrenheit on-demand
fahrenheit_pipeline = (
    {**reading, "fahrenheit": round((reading["celsius"] * 9/5) + 32, 2)}
    for reading in sensor_feed
)

# 3. Chain an anomaly gatekeeper filter to isolate critical overheating spikes
critical_spikes_pipeline = (
    metric for metric in fahrenheit_pipeline 
    if metric["celsius"] > 75.0
)

print("\n--- Sensor Event Stream Outlier Detection ---")
for critical_event in critical_spikes_pipeline:
    print(f"  [ALARM] Critical thermal spike detected! Payload: {critical_event}")

