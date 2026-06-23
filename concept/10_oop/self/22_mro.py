class BaseSystem(object):
    """The Grandparent Class (Top of the Diamond)"""
    def boot(self):
        print("[BaseSystem] Initializing core hardware sectors...")


class SecurityModule(BaseSystem):
    """Left Parent Node"""
    def boot(self):
        print("[SecurityModule] Running firewall checks...")
        # super() doesn't always mean 'go to immediate parent'. 
        # It means 'go to the next class in the computed MRO list'.
        super().boot()


class AnalyticsModule(BaseSystem):
    """Right Parent Node"""
    def boot(self):
        print("[AnalyticsModule] Spinning up data stream pipelines...")
        super().boot()


# ==========================================
# MULTIPLE INHERITANCE ASYMMETRY
# ==========================================
# The order you list parent classes inside the parentheses dictates their local priority.
# Because SecurityModule is written first, it receives evaluation priority.
class IntegratedDroneController(SecurityModule, AnalyticsModule):
    """The Child Class (Bottom of the Diamond)"""
    def boot(self):
        print(">>> Initiating Master Integrated Drone Boot Sequence...")
        super().boot()


# ==========================================
# EXPLORING THE RESOLUTION PATH
# ==========================================
print("--- Phase 1: Dynamic Execution Control ---")

controller = IntegratedDroneController()
controller.boot()


print("\n--- Phase 2: Introspecting the Linearization Lineup ---")

# You can access the flattened resolution order array at runtime using the.__mro__ attribute
mro_sequence = IntegratedDroneController.__mro__

for index, class_structure in enumerate(mro_sequence, start=1):
    print(f"Lookup Order Rank {index}: {class_structure.__name__}")