import sys

# ==========================================
# 1. THE LIFECYCLE & INTERACTION MODEL
# ==========================================

class DataPacket:
    def __init__(self, payload: str):
        """Object Lifecycle: Allocation/Creation Phase."""
        self.payload = payload  # Object State
        print(f"[Lifecycle - Creation] Memory allocated for DataPacket containing: '{self.payload}'")

    def extract_data(self):
        """Object Behavior."""
        return self.payload.upper()

    def __del__(self):
        """Object Lifecycle: Deallocation/Garbage Collection Phase."""
        print(f"[Lifecycle - Destruction] Object destroyed, freeing memory.")


class NetworkNode:
    def __init__(self, node_name: str):
        self.node_name = node_name

    def transmit(self, packet: DataPacket):
        """How Objects Interact: Passing an object reference as an argument."""
        processed_data = packet.extract_data()
        print(f"[Interaction] Node '{self.node_name}' processed data packet -> {processed_data}")


# ==========================================
# 2. RUNNING THE OBJECT MECHANICS DEMO
# ==========================================
print("--- Phase 1: Identity and Memory Representation ---")

# Instantiating a concrete object
my_packet = DataPacket("Initial Sync Signal")

# Introspecting Identity
print(f"Object Identity (RAM Address): {id(my_packet)} (Hex: {hex(id(my_packet))})")
print(f"Object Type: {type(my_packet)}")

# Reference Counting Check (How many pointers point to this memory block?)
# sys.getrefcount gives +1 because passing the object to the function briefly creates a temporary reference.
print(f"Reference count of my_packet: {sys.getrefcount(my_packet) - 1}")


print("\n--- Phase 2: Object Interactions ---")
node_alpha = NetworkNode("Router-01")

# Passing our data packet object into our network node object
node_alpha.transmit(my_packet)


print("\n--- Phase 3: Proof that Everything is an Object ---")

# In languages like C++ or Java, raw numbers like '42' are simple, primitive data types.
# In Python, even a raw integer or a standard function is a fully featured object in memory.
target_num = 42

print(f"Integer Identity: {id(target_num)}")
print(f"Integer Type: {type(target_num)}")
# We can look up available methods belonging directly to this raw number!
print(f"Does '42' have object methods? Yes! Bit length of 42 is: {target_num.bit_length()}")


print("\n--- Phase 4: Lifecycle Deallocation ---")
# To explicitly trigger the end of an object's life, we sever its pointer variables
print("Severing the final reference to my_packet...")
del my_packet  # Garbage collector immediately recovers the memory space since reference count drops to 0

# Wait a moment to observe terminal output
print("Script execution complete.")