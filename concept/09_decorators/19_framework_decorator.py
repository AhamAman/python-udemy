import functools
import inspect

# ==========================================
# 1. FLASK-STYLE ROUTE REGISTRATION SIMULATION
# ==========================================
class MockFlask:
    def __init__(self):
        # The central registry mapping URLs to functions
        self.routes = {}

    def route(self, rule: str, methods=["GET"]):
        """A decorator factory acting as an architectural registry."""
        def decorator(func):
            # We map the URL rule to the function object in our dictionary
            self.routes[rule] = {"handler": func, "methods": methods}
            
            @functools.wraps(func)
            def wrapper(*args, **kwargs):
                return func(*args, **kwargs)
            return wrapper
        return decorator


# ==========================================
# 2. FASTAPI-STYLE DEPENDENCY INJECTION SIMULATION
# ==========================================
class MockDepends:
    """Simulates FastAPI's Depends() token used for extracting dependencies."""
    def __init__(self, dependency_func):
        self.dependency_func = dependency_func

def inject_dependencies(func):
    """
    Simulates FastAPI's endpoint inspector that executes 
    Depends() parameters before running the actual function logic.
    """
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        # Use Python introspection to check parameters
        sig = inspect.signature(func)
        for param_name, param in sig.parameters.items():
            # If the default value is an instance of our Depends simulation
            if isinstance(param.default, MockDepends):
                # Resolve the dependency automatically
                resolved_dep = param.default.dependency_func()
                kwargs[param_name] = resolved_dep
                
        return func(*args, **kwargs)
    return wrapper


# ==========================================
# 3. CLICK-STYLE CLI COMMAND REGISTER SIMULATION
# ==========================================
class MockClickCLI:
    def __init__(self):
        self.commands = {}

    def command(self, name=None):
        def decorator(func):
            cmd_name = name or func.__name__
            self.commands[cmd_name] = {"func": func, "options": []}
            
            @functools.wraps(func)
            def wrapper(*args, **kwargs):
                return func(*args, **kwargs)
            return wrapper
        return decorator

    def option(self, flag: str, help_text: str):
        """Stacks configuration options onto the tracked command metadata."""
        def decorator(func):
            cmd_name = func.__name__
            # Since decorators execute bottom-to-top, we make sure the command exists
            if cmd_name not in self.commands:
                self.commands[cmd_name] = {"func": func, "options": []}
            
            self.commands[cmd_name]["options"].append({"flag": flag, "help": help_text})
            return func
        return decorator


# ==========================================
# 4. INITIALIZING AND USING THE MOCK FRAMEWORKS
# ==========================================
print("--- Phase 1: Framework Load & Registration Time ---")

app = MockFlask()
cli = MockClickCLI()

# --- A. Simulating Flask Router ---
@app.route("/api/v1/users", methods=["GET"])
def get_users():
    return [{"id": 1, "username": "alice"}]


# --- B. Simulating Click CLI Command Stacking ---
@cli.command(name="deploy")
@cli.option("--env", help_text="Target environment (prod/staging)")
@cli.option("--force", help_text="Skip confirmation checks")
def deploy_infrastructure(env="staging", force=False):
    print(f"   [CLI Core] Deploying with parameters -> Env: {env}, Force: {force}")


# --- C. Simulating FastAPI Route with Dependency Injection ---
def database_connection_provider():
    print("   [Dependency Pool] Allocating database transaction context...")
    return "<Active DB Client Object>"

@inject_dependencies
def read_secure_dashboard(db=MockDepends(database_connection_provider)):
    return f"Dashboard data retrieved using: {db}"


# ==========================================
# 5. SIMULATING RUNTIME DISPATCHING
# ==========================================
print("\n--- Phase 2: Framework Runtime Operations ---")

# 1. Simulating an incoming HTTP Request hits the Flask Routing table
requested_path = "/api/v1/users"
print(f"\n>>> Incoming Web Request for path: '{requested_path}'")
if requested_path in app.routes:
    route_info = app.routes[requested_path]
    response = route_info["handler"]() # Execute registered handler
    print(f"HTTP Response Generated: {response}")

# 2. Simulating a CLI invocation parsed by Click metadata
print("\n>>> System Terminal Command Executed: 'my_app deploy --env=prod'")
print(f"Registered CLI Configurations: {cli.commands['deploy']['options']}")
# Framework resolves flags and passes them down
cli.commands["deploy"]["func"](env="prod", force=True)

# 3. Simulating FastAPI automatic parameter injection
print("\n>>> Client executes 'read_secure_dashboard()' API endpoint")
# We do not provide the 'db' variable ourselves; our injection decorator handles it.
dashboard_response = read_secure_dashboard()
print(f"Final Payload: {dashboard_response}")