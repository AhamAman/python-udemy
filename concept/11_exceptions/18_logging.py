import logging
import json
import sys
import traceback
from datetime import datetime, timezone

# ==========================================
# 1. SETUP STRUCTURED JSON FORMATTING
# ==========================================

class JSONStructuredFormatter(logging.Formatter):
    """
    Custom logging formatter that serializes application state 
    and tracebacks into single-line JSON objects optimized for log search engines.
    """
    def format(self, record: logging.LogRecord) -> str:
        # Build the foundational log envelope payload
        log_payload = {
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "level": record.levelname,
            "logger": record.name,
            "message": record.getMessage(),
            "environment": "production",
            "service_name": "telemetry-ingestion-router"
        }

        # If an exception is attached to the log call, extract and serialize its data
        if record.exc_info:
            exc_type, exc_value, exc_traceback = record.exc_info
            
            log_payload["exception"] = {
                "class": exc_type.__name__ if exc_type else "UnknownException",
                "message": str(exc_value),
                # Flatten the multi-line stack trace list into an indexed array string
                "stack_trace": traceback.format_exception(exc_type, exc_value, exc_traceback)
            }

        # Inject injected contextual metadata attributes if present
        if hasattr(record, "request_id"):
            log_payload["request_id"] = record.request_id
        if hasattr(record, "user_id"):
            log_payload["user_id"] = record.user_id

        return json.dumps(log_payload)


# Initialize and configure our centralized structured logging pipe
logger = logging.getLogger("production_gateway")
logger.setLevel(logging.INFO)

# Direct log byte streams straight to standard stdout output streams
stream_handler = logging.StreamHandler(sys.stdout)
stream_handler.setFormatter(JSONStructuredFormatter())
logger.addHandler(stream_handler)


# ==========================================
# 2. RUNNING LIVE CORE DISPATCH EXPERIMENTS
# ==========================================

def process_cloud_telemetry_packet(raw_data: dict, client_context: dict):
    """Volatile infrastructure runner logging structural outcomes."""
    
    # We bind global transaction metadata tokens to pass into our logging record layers
    log_meta = {
        "extra": {
            "request_id": client_context.get("req_id"),
            "user_id": client_context.get("user_id")
        }
    }

    try:
        logger.info("Initiating structural decoding pass for telemetry matrix item.", **log_meta)
        
        # Trigger an intentional structural validation crash
        calculated_metric = raw_data["metric_reading"] / raw_data["divisor_offset"]
        logger.info(f"Telemetry metric computed cleanly: {calculated_metric}", **log_meta)

    # ==========================================
    # LOGGING EXCEPTION DETAILS CORRECTLY
    # ==========================================
    except ZeroDivisionError as math_fault:
        # Crucial Pattern: Using logger.error with exc_info=True explicitly instructs
        # the logging engine to capture the active system traceback from memory.
        logger.error(
            "Mathematical boundary violation: Refusing execution over zero divisor offsets.",
            exc_info=True, 
            **log_meta
        )
        
    except KeyError as schema_fault:
        logger.error(
            f"Incoming payload schema missing mandatory transactional mapping key: {schema_fault}",
            exc_info=True,
            **log_meta
        )


# Run Suite Pass A: Triggers a ZeroDivisionError
sample_ctx = {"req_id": "REQ-88941-X", "user_id": "USR-ALPHA-09"}
process_cloud_telemetry_packet({"metric_reading": 550.4, "divisor_offset": 0}, sample_ctx)

# Run Suite Pass B: Triggers a KeyError
process_cloud_telemetry_packet({"malformed_fields_present": True}, sample_ctx)