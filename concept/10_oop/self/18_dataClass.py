from dataclasses import dataclass, field
from typing import List

# ==========================================
# 1. THE FOUNDATIONAL DATACLASS
# ==========================================
@dataclass
class InventoryItem:
    """
    A standard dataclass. Python automatically builds:
    __init__, __repr__, and __eq__ based on these type hints.
    """
    name: str
    sku: str
    unit_price: float
    quantity: int = 0  # Standard default value

    # For mutable defaults (like lists or dicts), you CANNOT use standard defaults:
    # tags: List[str] = [] <-- This is a syntax error because it creates a shared mutable state!
    # Instead, use field(default_factory=...) to generate a clean list for every instance:
    tags: List[str] = field(default_factory=list)


# ==========================================
# 2. IMMUTABILITY (Frozen Dataclasses)
# ==========================================
@dataclass(frozen=True)
class ImmutableConfiguration:
    """
    Setting frozen=True makes instances read-only.
    It automatically generates __setattr__ and __delattr__ methods that raise errors on mutation.
    """
    api_endpoint: str
    timeout_seconds: int = 30


# ==========================================
# 3. DATACLASS INHERITANCE
# ==========================================
@dataclass
class PerishableItem(InventoryItem):
    """
    Inherits fields from InventoryItem. 
    Python combines them sequentially for the generated constructor.
    """
    expiration_date: str = "2026-12-31"


# ==========================================
# RUNNING THE DATACLASS ECOSYSTEM
# ==========================================
print("--- Phase 1: Automatic Method Generation ---")

item_a = InventoryItem("Alpha Sensor", "SNS-001", 49.99, 10, ["hardware", "telemetry"])
item_b = InventoryItem("Alpha Sensor", "SNS-001", 49.99, 10, ["hardware", "telemetry"])

# 1. Automatic __repr__ (Prints a beautifully formatted string instead of <__main__.Object at 0x...>)
print(f"Auto-generated Representation:\n   {item_a}")

# 2. Automatic __eq__ (Compares values directly, not memory addresses)
print(f"\nAre item_a and item_b structurally identical? {item_a == item_b}")


print("\n--- Phase 2: Testing Immutability Guardrails ---")
config = ImmutableConfiguration(api_endpoint="https://gateway.internal")
print(f"Read access allowed: {config.api_endpoint}")

try:
    # This write attempt will be caught by the frozen guardrail
    config.timeout_seconds = 60
except Exception as e:
    print(f"❌ Modification Blocked Safely: {type(e).__name__} - Cannot modify frozen dataclass attributes.")


print("\n--- Phase 3: Dataclass Inheritance Evaluation ---")
# The generated constructor puts base parameters first, then subclass parameters
milk = PerishableItem("Organic Milk", "MLK-99", 3.49, 100, ["dairy"], "2026-07-15")
print(f"Perishable Item Setup: {milk}")