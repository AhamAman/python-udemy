def alert_monitor(threshold):
    print("[Coroutine] Active. Listening for metrics...")
    try:
        while True:
            # Pauses here, waiting exclusively to CONSUME data
            metric = yield
            
            if metric > threshold:
                print(f"🚨 ALERT: Metric {metric} exceeded threshold of {threshold}!")
            else:
                print(f"✅ Metric {metric} is nominal.")
    except GeneratorExit:
        print("[Coroutine] Shutting down monitor.")

# --- Execution ---
monitor = alert_monitor(threshold=100)

# Prime it to reach the `yield` line
next(monitor) 

# Stream data into it dynamically
monitor.send(45)   # ✅ Metric 45 is nominal.
monitor.send(120)  # 🚨 ALERT: Metric 120 exceeded threshold!
monitor.close()    # Shut down