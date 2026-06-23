import threading
import time
import random

class BankAccount:
    def __init__(self, account_name, initial_balance):
        self.name = account_name
        self.balance = initial_balance

    def withdraw(self, amount, customer_name):
        print(f"  [{customer_name}] Checking balance... Current: ${self.balance}")
        
        # Check if funds are available
        if self.balance >= amount:
            print(f"  [{customer_name}] Approved! Processing payout of ${amount}...")
            
            # Context switch window
            time.sleep(random.uniform(0.001, 0.005))
            
            # Deduct the balance
            self.balance -= amount
            print(f"  [{customer_name}] Transaction Complete. New Balance: ${self.balance}")
        else:
            print(f"  [{customer_name}] Declined! Insufficient funds.")

if __name__ == "__main__":
    # Start an account with $100
    shared_account = BankAccount("Joint Account", 100)
    
    print(f"Initial Account Balance: ${shared_account.balance}")
    print("Husband and Wife try to withdraw $80 at the exact same fraction of a second...\n")
    
    # Spawn two threads executing withdrawals concurrently
    t1 = threading.Thread(target=shared_account.withdraw, args=(80, "Husband"))
    t2 = threading.Thread(target=shared_account.withdraw, args=(80, "Wife"))
    
    t1.start()
    t2.start()
    
    t1.join()
    t2.join()
    
    print("\n--- Final Account Audit ---")
    print(f"Expected ending balance if safe:  $20 (One transaction should decline)")
    print(f"Actual balance in database:      ${shared_account.balance}")
    
    if shared_account.balance < 0:
        print("CRITICAL ERROR: Account went into negative debt due to a Race Condition!")