import threading
import queue
import time
import random

# Thread-safe FIFO Queue
email_queue = queue.Queue()

def background_email_worker():
    print("  [Worker Thread] Email engine started and listening...")
    while True:
        # Blocks indefinitely until an item arrives
        email_task = email_queue.get()
        
        # Check for a sentinel/poison pill to shut down gracefully
        if email_task is None:
            email_queue.task_done()
            break
            
        user, email_type = email_task
        print(f"  [Worker Thread] [SENDING] {email_type} email to {user}...")
        
        # Simulate network latency of talking to an email server
        time.sleep(random.uniform(0.5, 1.0))
        
        print(f"  [Worker Thread] [SUCCESS] {email_type} delivered to {user}.")
        email_queue.task_done()
        
    print("  [Worker Thread] Email engine stopped cleanly.")

if __name__ == "__main__":
    # Start the permanent background email processor
    worker = threading.Thread(target=background_email_worker, daemon=True)
    worker.start()
    
    print("[Main Thread UI] User clicks 'Sign Up'.")
    email_queue.put(("alice@example.com", "Welcome"))
    
    print("[Main Thread UI] User clicks 'Forgot Password'.")
    email_queue.put(("bob@example.com", "Password Reset"))
    
    time.sleep(0.2)
    print("[Main Thread UI] User updates billing info.")
    email_queue.put(("charlie@example.com", "Invoice Paid"))
    
    print("[Main Thread UI] Interface is completely responsive. User continues browsing...")
    
    # Wait for all emails to send
    email_queue.join()
    
    # Shut down the background thread cleanly using a "poison pill"
    email_queue.put(None)
    worker.join()
    print("=== PIPELINE SHUTDOWN ===")