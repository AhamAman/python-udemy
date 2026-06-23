import time

class SensorCluster:
    def __init__(self, cluster_id: str, hardware_nodes: list):
        # 1. __init__: The Object Initializer
        # Populates the blank instance memory block with attributes
        print(f"[__init__] Initializing instance state for Cluster '{cluster_id}'")
        self.cluster_id = cluster_id
        self.nodes = list(hardware_nodes)

    # ==========================================
    # STRING & REPRESENTATION MANAGEMENT
    # ==========================================

    def __str__(self) -> str:
        # 2. __str__: User-Facing String Representation
        # Invoked via str(obj) or print(obj). Optimized for human readability.
        return f"SensorCluster '{self.cluster_id}' running {len(self.nodes)} nodes"

    def __repr__(self) -> str:
        # 3. __repr__: Developer/Ambiance Representation
        # Invoked via repr(obj) or inside interactive terminals. 
        # Goal is to be unambiguous, showing exactly how to recreate the object.
        return f"SensorCluster(cluster_id='{self.cluster_id}', hardware_nodes={self.nodes})"

    # ==========================================
    # COLLECTION MECHANICS
    # ==========================================

    def __len__(self) -> int:
        # 4. __len__: Exposes sizing data
        # Invoked via len(obj). Must return a non-negative integer.
        return len(self.nodes)

    def __bool__(self) -> bool:
        # 5. __bool__: Truth value assessment
        # Invoked via bool(obj) or 'if obj:'.
        # If omitted, Python falls back to checking __len__ automatically.
        return len(self.nodes) > 0

    def __contains__(self, item: str) -> bool:
        # 9. __contains__: Membership testing
        # Invoked via 'item in obj'.
        print(f"   [__contains__] Checking registry for node reference: '{item}'")
        return item in self.nodes

    def __iter__(self):
        # 10. __iter__: Iteration controller
        # Invoked via loops 'for x in obj:'. Returns an iterator object.
        print("   [__iter__] Generating sequence stream...")
        return iter(self.nodes)

    # ==========================================
    # COMPARISONS & HASHING (Ordering Models)
    # ==========================================

    def __eq__(self, other) -> bool:
        # 6. __eq__: Structurally Equal (==)
        if not isinstance(other, SensorCluster):
            return False
        return self.cluster_id == other.cluster_id

    def __lt__(self, other) -> bool:
        # 7. __lt__: Less Than (<)
        if not isinstance(other, SensorCluster):
            raise TypeError("Comparison only supported between identical types.")
        return len(self.nodes) < len(other.nodes)

    def __gt__(self, other) -> bool:
        # 8. __gt__: Greater Than (>)
        if not isinstance(other, SensorCluster):
            raise TypeError("Comparison only supported between identical types.")
        return len(self.nodes) > len(other.nodes)

    def __hash__(self) -> int:
        # 12. __hash__: Object signature identity computation
        # Invoked when object is placed into sets or used as keys in a dict.
        # Immutability note: An object should only be hashable if its eq attributes never change.
        return hash(self.cluster_id)

    # ==========================================
    # ADVANCED FUNCTIONAL UTILITIES
    # ==========================================

    def __call__(self, ping_payload: str):
        # 11. __call__: Makes the instance invokeable like a function
        # Invoked via cluster_instance("payload")
        print(f"\n[__call__] Executing dynamic broadcast sweep: '{ping_payload}'")
        return f"Ping sequence delivered to nodes: {self.nodes}"

    def __del__(self):
        # 14. __del__: The Deallocator Destructor
        # Triggered when reference count reaches 0 right before memory reclamation.
        print(f"[__del__] Freeing resources for cluster '{self.cluster_id}'. Offline.")


# ==========================================
# TESTING THE INTERFACES
# ==========================================
print("--- Phase 1: Creation and Strings ---")
cluster_alpha = SensorCluster("Alpha-Net", ["Node-01", "Node-02", "Node-03"])
cluster_beta  = SensorCluster("Beta-Net", ["Node-99"])

# Striking string representation pipelines
print(f"str() display:  {cluster_alpha}")
print(f"repr() display: {repr(cluster_alpha)}")


print("\n--- Phase 2: Sizing and Booleans ---")
print(f"Length evaluation: {len(cluster_alpha)}")
if cluster_alpha: # Uses __bool__
    print("Cluster Alpha is evaluated as: TRUE (Active)")


print("\n--- Phase 3: Comparisons & Collection Mechanics ---")
# Using standard algebraic operators directly on custom class objects
print(f"Is Alpha equal to Beta?   {cluster_alpha == cluster_beta}")
print(f"Is Alpha bigger than Beta? {cluster_alpha > cluster_beta}")

# Using membership containment checks
if "Node-02" in cluster_alpha:
    print("   Locality hit!")

# Iterating using native python loop structure
print("\nExecuting native sequence loop mapping:")
for node in cluster_alpha:
    print(f"   Node point: {node}")


print("\n--- Phase 4: Callable Invocations & Hashing ---")
# Treating the object instance exactly like a function call
response = cluster_alpha("Telemetry Check Code 200")
print(f"Invocation Result: {response}")

# Using object as a dictionary key (Requires __hash__ and __eq__)
system_registry = {cluster_alpha: "Online-Verified"}
print(f"Lookup via object instance: {system_registry[cluster_alpha]}")


print("\n--- Phase 5: Destructor Termination ---")
# Sever references to trace memory destruction
del cluster_alpha
del cluster_beta