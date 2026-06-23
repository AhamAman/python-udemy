# ==========================================
# 1. DEFINE THREE COMPLETELY UNRELATED CLASSES
# ==========================================

class EncryptedFileStream:
    """A backend data layer storage utility."""
    def read(self) -> str:
        print("[Crypto Stream] Decrypting bytes from on-disk blocks...")
        return "Decrypted: Data Stream Payload"


class MockNetworkSocket:
    """A networking utility that mimics a stream."""
    def read(self) -> str:
        print("[Network Socket] Compiling raw TCP packets from socket buffer...")
        return "Network: Packet Payload"


class BrokenSystemTool:
    """A tool that has a matching name but returns wrong types."""
    def read(self) -> int:
        print("[System Tool] Intercepting metrics...")
        return 500


# ==========================================
# 2. THE DUCK-TYPED PIPELINE (The Consumer)
# ==========================================

def ingest_data_source(stream_object):
    """
    This function relies entirely on Duck Typing.
    It does not care what class stream_object belongs to, as long as it 
    'quacks' like a readable stream by providing a .read() method.
    """
    print(f"\n>>> Ingesting source type: {type(stream_object).__name__}")
    
    # Python doesn't check types ahead of time. It attempts the call at runtime.
    data = stream_object.read()
    print(f"    Ingested Data Outcome: {data}")


# ==========================================
# 3. RUNNING THE EXECUTION ENGINE
# ==========================================
print("--- Phase 1: Successful Dynamic Processing ---")

file_stream = EncryptedFileStream()
network_stream = MockNetworkSocket()

# Both work seamlessly despite sharing absolutely NO common parent class
ingest_data_source(file_stream)
ingest_data_source(network_stream)


print("\n--- Phase 2: Analyzing the Risks of Duck Typing ---")

# Risk 1: Semantic misunderstandings (Wrong return types or behaviors)
# BrokenSystemTool has a .read() method, so it passes the basic duck test, 
# but it returns an integer instead of a string, which could break downstream string manipulation.
tool_stream = BrokenSystemTool()
ingest_data_source(tool_stream)


# Risk 2: Runtime Crash (AttributeError)
# If an object completely lacks the required method, the error is caught only 
# when that specific line of code executes at runtime.
class SimpleString:
    def __init__(self):
        self.text = "I am a basic string with no read method."

dead_duck = SimpleString()

try:
    ingest_data_source(dead_duck)
except AttributeError as e:
    print(f"❌ Runtime Crash Caught: {e}")