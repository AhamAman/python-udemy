import sys

# ==========================================
# 1. CORE TYPE & VALUE EXTREMES
# ==========================================

def trigger_value_error():
    # ValueError: Raised when an operation receives an argument of the correct 
    # type but an inappropriate or invalid value value.
    print("\n[Simulating ValueError]")
    int("not_a_number_string")  # Type is string (valid input shape), but value cannot be cast to base-10 int.

def trigger_type_error():
    # TypeError: Raised when an operation is applied to an object of an inappropriate type.
    print("\n[Simulating TypeError]")
    len(42)  # Integers do not possess a length descriptor; len() demands an iterable sequence.


# ==========================================
# 2. LOOKUP BOUNDARY ERRORS
# ==========================================

def trigger_index_error():
    # IndexError: Raised when a sequence subscript index is out of range.
    print("\n[Simulating IndexError]")
    sample_list = [10, 20]
    _ = sample_list[5]  # Index 5 does not exist in a 2-element sequence.

def trigger_key_error():
    # KeyError: Raised when a dictionary key is not found in the set of existing keys.
    print("\n[Simulating KeyError]")
    sample_dict = {"id": 101}
    _ = sample_dict["status"]  # The mapping collection lacks this specific lookup token.


# ==========================================
# 3. INTERACTION & SCOPE ERRORS
# ==========================================

def trigger_attribute_error():
    # AttributeError: Raised when an attribute reference or assignment fails.
    print("\n[Simulating AttributeError]")
    text_string = "hello"
    text_string.append(" world")  # Strings are immutable and lack an .append() method.

def trigger_name_error():
    # NameError: Raised when a local or global name is not found in the current scope.
    print("\n[Simulating NameError]")
    print(undefined_variable_token)  # Referencing a variable that was never declared in memory.


# ==========================================
# 4. MATH & ARCHITECTURAL RUNTIMES
# ==========================================

def trigger_zero_division_error():
    # ZeroDivisionError: Raised when the second argument of a division or modulo operation is zero.
    print("\n[Simulating ZeroDivisionError]")
    _ = 1 / 0  # Mathematically undefined boundary in integer arithmetic.

def trigger_runtime_error():
    # RuntimeError: A generic fallback exception raised when an error doesn't 
    # fit cleanly into any other specific exception category.
    print("\n[Simulating RuntimeError]")
    raise RuntimeError("An unpredictable internal processing sequence split failed.")


# ==========================================
# 5. ENVIRONMENT & OPERATING SYSTEM ERRORS
# ==========================================

def trigger_os_errors():
    # OSError: The base parent class for system-level errors (file missing, permissions, etc.).
    # FileNotFoundError: Child of OSError. Raised when a file is requested but cannot be located.
    print("\n[Simulating FileNotFoundError]")
    open("ghost_file_directory_999.txt", "r")

def trigger_permission_error():
    # PermissionError: Child of OSError. Raised when trying to access a file without OS authorization.
    print("\n[Simulating PermissionError]")
    # On most operating systems, writing directly to the root directory requires admin elevations
    open("/system_protected_root.log", "w")

def trigger_timeout_error():
    # TimeoutError: Child of OSError. Raised when a system function times out at the OS level.
    print("\n[Simulating TimeoutError]")
    import socket
    sock = socket.socket()
    sock.settimeout(0.001)
    sock.connect(("1.1.1.1", 80)) # Will drop immediately via timeout parameters


# ==========================================
# 6. INTEGRATION & MODULE ERRORS
# ==========================================

def trigger_import_errors():
    # ImportError: Raised when an import statement fails to load a module or a name inside a module.
    # ModuleNotFoundError: A modern specific child of ImportError raised when the package cannot be found at all.
    print("\n[Simulating ModuleNotFoundError]")
    import non_existent_cloud_analytics_library


# ==========================================
# 7. METRIC HARDWARE LIMIT COMPILATIONS
# ==========================================

def trigger_recursion_error():
    # RecursionError: Raised when the interpreter detects that the maximum recursion depth has been exceeded.
    print("\n[Simulating RecursionError]")
    def infinite_loop():
        return infinite_loop()
    infinite_loop()

def trigger_memory_error():
    # MemoryError: Raised when an operation runs out of physical RAM but the interpreter can still recover.
    print("\n[Simulating MemoryError]")
    # Creating a massive allocation block that outstrips default memory maps
    _ = bytearray(10**14) 


# ==========================================
# SIMULATION ENGINE ROUTER
# ==========================================
experiments = [
    trigger_value_error, trigger_type_error, trigger_index_error, 
    trigger_key_error, trigger_attribute_error, trigger_name_error, 
    trigger_zero_division_error, trigger_runtime_error, trigger_os_errors, 
    trigger_permission_error, trigger_timeout_error, trigger_import_errors, 
    trigger_recursion_error, trigger_memory_error
]

print("--- Executing System Exception Profile Tests ---")
for experiment in experiments:
    try:
        experiment()
    except Exception as e:
        print(f"   ↳ Caught Exception Signature: {type(e).__name__} -> {e}")