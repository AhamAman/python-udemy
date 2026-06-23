import inspect

def monitor_system_frame_telemetry():
    """Inner worker executing sub-routine tasks."""
    local_worker_metric = 451.92
    local_status_flag = "PROCESSING"
    
    print("--- 1. Introspecting Current Active Frame ---")
    
    # Capture the live frame object currently executing at this exact millisecond
    current_frame = inspect.currentframe()
    
    print(f"Current Function Frame Name: '{current_frame.f_code.co_name}'")
    print(f"Local Scope Storage Dump:     {current_frame.f_locals}")
    
    print("\n--- 2. Traversing Upwards via the Return Pointer ---")
    # f_back reads the return pointer to look at the calling parent frame
    parent_frame = current_frame.f_back
    print(f"Parent Caller Frame Name:    '{parent_frame.f_code.co_name}'")
    print(f"Parent Local Scope Elements:  {parent_frame.f_locals}")


def orchestrate_pipeline_run(execution_id):
    """Parent controller function that pushes onto the stack."""
    pipeline_configuration_tier = "SECURE_ALPHA"
    
    # Calling this function pauses orchestrate_pipeline_run and pushes monitor onto the stack
    monitor_system_frame_telemetry()


# Kick off the execution lifecycle
orchestrate_pipeline_run(execution_id=9004)