# ==========================================
# 1. CLASS IMPLEMENTATION (Single Inheritance Pipeline)
# ==========================================

class NetworkService:
    """The Parent/Base Class managing connections."""
    def __init__(self, endpoint: str):
        print(f"[Base Init] Setting up endpoint network routing for: {endpoint}")
        self.endpoint = endpoint
        self.is_connected = False

    def connect(self):
        """A core method intended to be extended by subclasses."""
        print(f"[Base Connect] Establishing handshakes to {self.endpoint}...")
        self.is_connected = True
        return self.is_connected


class EncryptedNetworkService(NetworkService):
    """The Child Class extending and securing connection behavior."""
    def __init__(self, endpoint: str, cipher_key: str):
        # 1. CALLING PARENT CONSTRUCTOR
        # Instead of writing NetworkService.__init__(self, endpoint), we use super().
        # This shields us from structural changes if the parent class name changes later.
        super().__init__(endpoint)
        
        print("[Child Init] Securing local environment with encryption cipher.")
        self.cipher_key = cipher_key

    def connect(self):
        # 2. EXTENDING PARENT METHOD
        # We wrap the parent's base connection execution with custom child logic.
        print("\n[Child Connect] Intercepting request to apply SSL/TLS wrapping...")
        
        # Invoke the parent's connection algorithm using super()
        base_success = super().connect()
        
        if base_success:
            print(f"[Child Connect] Enforcing cryptographic key validation: {self.cipher_key[:4]}****")
            print("[Child Connect] Status: Connection fully encrypted and secure.")
        return base_success


# ==========================================
# 2. RUNNING THE CODE
# ==========================================
print("--- Phase 1: Object Instantiation ---")
secure_conn = EncryptedNetworkService(endpoint="https://api.secure-vault.internal", cipher_key="AES_256_GCM")

print("\n--- Phase 2: Method Overriding & super() Traversal ---")
secure_conn.connect()


print("\n--- Phase 3: Introspecting the Method Resolution Order (MRO) ---")
# Let's peek into the real runtime sequence Python follows to resolve lookups
for index, class_obj in enumerate(EncryptedNetworkService.__mro__, start=1):
    print(f" MRO Step {index}: {class_obj}")