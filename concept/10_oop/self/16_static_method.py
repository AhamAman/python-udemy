import re

class NetworkPacket:
    # Class-level configuration constants
    MAX_ALLOWED_SIZE_BYTES = 1024

    def __init__(self, payload: str, destination_ip: str):
        # Instance validation logic relying on our static method utility
        if not self.is_valid_ip(destination_ip):
            raise ValueError(f"Invalid routing configuration: '{destination_ip}'")
            
        self.payload = payload
        self.ip = destination_ip

    # ==========================================
    # 1. THE STATIC METHOD (Isolated Utility)
    # ==========================================
    @staticmethod
    def is_valid_ip(ip_address: str) -> bool:
        """
        A pure utility function. 
        It does not look at self.payload or cls.MAX_ALLOWED_SIZE_BYTES.
        It takes an input, runs logic, and returns an output independently.
        """
        print(f"   [Static Method] Validating IP string constraint: '{ip_address}'")
        # Simple regex matching an IPv4 layout
        pattern = r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$"
        return bool(re.match(pattern, ip_address))

    # ==========================================
    # 2. CONTRASTING CLASS AND INSTANCE METHODS
    # ==========================================
    @classmethod
    def create_broadcast_packet(cls, payload: str):
        """Class Method: Needs 'cls' to build a factory instantiation."""
        print("\n[Class Method Factory] Generating broadcast structure...")
        return cls(payload=payload, destination_ip="255.255.255.255")

    def dispatch(self):
        """Instance Method: Needs 'self' to extract current object data attributes."""
        print(f"\n[Instance Method] Dispatching packet to {self.ip} | Payload: {self.payload}")


# ==========================================
# RUNNING THE METHOD NAMESPACE DEMO
# ==========================================
print("--- Phase 1: Calling Static Methods Independently ---")

# Crucial Design Benefit: You do NOT need to instantiate an object to use a static method.
# It functions as a clean namespace utility.
is_ok = NetworkPacket.is_valid_ip("192.168.1.1")
print(f"Validation Check Result: {is_ok}")


print("\n--- Phase 2: Utilizing the Full Method Ecosystem ---")

# 1. Class factory method creates the object instance internally
packet_obj = NetworkPacket.create_broadcast_packet("System Update Signal")

# 2. Instance method executes operations based on specific object attributes
packet_obj.dispatch()


print("\n--- Phase 3: Defensive Instantiation Verification ---")
try:
    print("\nAttempting to build packet with malformed routing address...")
    broken_packet = NetworkPacket(payload="Data", destination_ip="999.BAD.IP.999")
except ValueError as e:
    print(f"❌ Core Initializer Blocked: {e}")