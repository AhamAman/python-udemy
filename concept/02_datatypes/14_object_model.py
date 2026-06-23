import sys
import gc

# ==========================================
# 1. Peeking at Reference Counts
# ==========================================
print("--- Reference Counting Mechanics ---")

# Create a brand new list object
sample_data = [10, 20, 30]

# Check reference count. 
# NOTE: sys.getrefcount() temporarily borrows the object, adding +1 to the count!
print(f"Initial reference count (Expected ~2): {sys.getrefcount(sample_data)}")

# Create an alias (Shared reference)
alias_pointer = sample_data
print(f"Count after assigning alias (Expected ~3): {sys.getrefcount(sample_data)}")


# ==========================================
# 2. Breaking a Reference Count Down to Zero
# ==========================================
print("\n--- The Path to Deallocation ---")

class Asset:
    def __init__(self, name):
        self.name = name
    def __del__(self):
        # This destructor method executes right before memory is wiped
        print(f"☠️ Hardware Alert: Memory for '{self.name}' has been freed!")

# Born: Object allocated in RAM
item = Asset("Core Database Pointer")

# Drop the reference count by reassigning the variable name
print("Reassigning 'item' variable to None...")
item = None  # Ref count hits 0 -> Triggers instantaneous deallocation!


# ==========================================
# 3. Generating and Clearing a Cyclic Memory Leak
# ==========================================
print("\n--- Circular Reference and the GC ---")

class Node:
    def __init__(self, id):
        self.id = id
        self.connected_to = None
    def __del__(self):
        print(f"☠️ GC Alert: Node {self.id} destroyed!")

# Create two independent nodes
node_a = Node(1)
node_b = Node(2)

# Establish a circular reference trap
node_a.connected_to = node_b
node_b.connected_to = node_a

print("Severing external variable names...")
# Delete external access labels
del node_a
del node_b

# Observation: The destructors did NOT run above! They are trapped in memory.
print("Explicitly invoking the Generational Garbage Collector...")
gc.collect() # Forces the cyclical GC engine to hunt down memory leaks