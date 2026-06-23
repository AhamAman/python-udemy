# ==========================================
# 1. Functions as Assignable Objects
# ==========================================
print("--- 1. Variable Assignment ---")

def engine_ignition():
    return "Core Reactor: IGNITED"

# Assignment: 'launcher' now points to the exact same memory ID as 'engine_ignition'
launcher = engine_ignition

print(f"Original Function ID: {id(engine_ignition)}")
print(f"Variable Pointer ID:  {id(launcher)}")
print(f"Executing via alias:  {launcher()}")


# ==========================================
# 2. Passing Functions as Arguments
# ==========================================
print("\n--- 2. Higher-Order Functions ---")

def standard_formatter(text):
    return f"[LOG] {text.upper()}"

def executing_pipeline(worker_function, message_payload):
    """Accepts a function object as its first parameter."""
    # Executes the injected function behavior dynamically at runtime
    return worker_function(message_payload)

# Injecting the 'standard_formatter' block directly into the pipeline
pipeline_result = executing_pipeline(standard_formatter, "system warning node 4")
print(pipeline_result)


# ==========================================
# 3. Storing Functions in Data Structures
# ==========================================
print("\n--- 3. Router Table Data Structure ---")

def step_add(x, y): return x + y
def step_sub(x, y): return x - y
def step_mul(x, y): return x * y

# Mapping string command keys straight to the un-executed function objects
math_router_table = {
    "ADD": step_add,
    "SUB": step_sub,
    "MUL": step_mul
}

# Dynamic, flat execution routing table without any if-elif-else bloat
operation = "MUL"
targeted_function = math_router_table[operation]
print(f"Router Output ({operation}): {targeted_function(10, 5)}")


# ==========================================
# 4. Returning Functions (The Factory Pattern)
# ==========================================
print("\n--- 4. Function Factories ---")

def generate_power_multiplier(exponent):
    """Generates and returns a customized dynamic function."""
    def multiplier_instance(base_number):
        return base_number ** exponent
    
    return multiplier_instance # Returning the inner function object itself

# Constructing two entirely independent calculations
cube_calculator = generate_power_multiplier(3)
quad_calculator = generate_power_multiplier(4)

print(f"2 Cubed: {cube_calculator(2)}")  # 2^3 = 8
print(f"2 Quad:  {quad_calculator(2)}")  # 2^4 = 16