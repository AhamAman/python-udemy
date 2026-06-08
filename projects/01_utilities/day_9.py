"""
Challenge: Set a Countdown Timer

Create a Python script that allows the user to set a timer in seconds. The script should:

1. Ask the user for the number of seconds to set the timer.
2. Show a live countdown in the terminal.
3. Notify the user when the timer ends with a final message and sound (if possible).

Bonus:
- Format the remaining time as MM:SS
- Use a beep sound (`\a`) at the end if the terminal supports it
- Prevent negative or non-integer inputs
"""

import time
import tkinter as tk
from tkinter import messagebox

def get_total_seconds():
    """Prompts user for minutes and seconds, returning total duration in seconds."""
    print("⏳ Set your timer:")
    while True:
        try:
            minutes = int(input("   Enter minutes: ") or 0)
            seconds = int(input("   Enter seconds: ") or 0)
            
            total = (minutes * 60) + seconds
            if total <= 0:
                print("❌ Please enter a duration greater than 0 seconds.\n")
                continue
            return total
        except ValueError:
            print("❌ Invalid input. Please enter whole numbers only.\n")

def trigger_alarm():
    """Creates a non-blocking pop-up notification window when time is up."""
    # Hide the main root window of tkinter
    root = tk.Tk()
    root.withdraw()
    root.attributes("-topmost", True)  # Force it to appear on top of other windows
    
    messagebox.showinfo("⏰ Time's Up!", "Take a break or move on to your next task.")
    root.destroy()

def run_timer(total_seconds):
    print("\n🔔 Timer started...")
    
    # We keep track of the initial time to calculate progress
    initial_seconds = total_seconds 
    
    for remaining in range(total_seconds, -1, -1):
        mins, secs = divmod(remaining, 60)
        time_format = f"{mins:02}:{secs:02}"
        
        # Create a simple visual progress bar (10 blocks wide)
        elapsed = initial_seconds - remaining
        progress_ratio = elapsed / initial_seconds if initial_seconds > 0 else 1
        bar_length = 10
        filled_length = int(round(bar_length * progress_ratio))
        bar = '█' * filled_length + '-' * (bar_length - filled_length)
        
        # The extra spaces at the end prevent ghost characters on the terminal
        print(f"🕰️  [{bar}] {time_format} left    ", end="\r")
        
        if remaining > 0:
            time.sleep(1)
            
    print("\n\n🎉 Finished!")
    trigger_alarm()

def main():
    try:
        total_time = get_total_seconds()
        run_timer(total_time)
    except KeyboardInterrupt:
        # Gracefully handle Ctrl+C without throwing an ugly stack trace
        print("\n\n🛑 Timer cancelled by user. Goodbye!")

if __name__ == "__main__":
    main()