import json

# ==========================================
# APPROACH 1: INHERITANCE-BASED POLYMORPHISM
# ==========================================

class MediaExporter:
    """The parent blueprint establishing a common interface."""
    def export(self, data: dict) -> str:
        raise NotImplementedError("Subclasses must implement the export method.")


class JSONExporter(MediaExporter):
    """Specialized exporter that overrides parent behavior."""
    def export(self, data: dict) -> str:
        print("[JSON Engine] Serializing structured payload to minified JSON string...")
        return json.dumps(data)


class CSVExporter(MediaExporter):
    """Specialized exporter that overrides parent behavior."""
    def export(self, data: dict) -> str:
        print("[CSV Engine] Flattening payload to comma-separated values stream...")
        # Simple transform converting keys to header and values to a line
        headers = ",".join(data.keys())
        values = ",".join(str(v) for v in data.values())
        return f"{headers}\n{values}"


# ==========================================
# APPROACH 2: DUCK TYPING POLYMORPHISM (No Shared Parent)
# ==========================================

class S3CloudUploader:
    """Isolated infrastructure class. Does NOT inherit from MediaExporter."""
    def export(self, data: dict) -> str:
        print("[S3 Cloud Engine] Direct streaming raw dictionary bytes to cloud bucket storage...")
        return f"s3://bucket-hash/payload.data"


# ==========================================
# 3. HIGH-LEVEL PIPELINE EXECUTION (The Client Code)
# ==========================================

def process_and_dispatch(exporter_engine, application_state: dict):
    """
    This client function displays the true power of polymorphism.
    It has ZERO knowledge of concrete exporter types. It only requires 
    that the passed 'exporter_engine' possesses an .export() method.
    """
    print(f"\n>>> Initializing dispatch pipeline using engine: {type(exporter_engine).__name__}")
    
    # Polymorphic Execution: The behavior changes dynamically based on the object type
    output_string = exporter_engine.export(application_state)
    
    print(f"Pipeline Transmission Complete. Output Length: {len(output_string)} units.")


# ==========================================
# 4. TESTING THE POLYMORPHIC PIPELINE
# ==========================================
print("--- Execution Phase ---")

mock_payload = {"user_id": 9941, "action": "checkout", "credits_spent": 14.50}

# Instantiating our diverse asset family
json_tool = JSONExporter()
csv_tool = CSVExporter()
cloud_tool = S3CloudUploader() # The duck-typed outsider

# 1. Pipeline runs Inheritance-based polymorphic objects
process_and_dispatch(json_tool, mock_payload)
process_and_dispatch(csv_tool, mock_payload)

# 2. Pipeline runs Duck-Typed object seamlessly
# This works flawlessly because Python is dynamically typed and evaluates signatures at runtime
process_and_dispatch(cloud_tool, mock_payload)