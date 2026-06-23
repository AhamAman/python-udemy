import asyncio
import time
from fastapi import FastAPI, Depends, WebSocket, WebSocketDisconnect

app = FastAPI(title="Accelerated Async Web Engine")

# =====================================================================
# DEPENDENCY INJECTION LAYER (Shared Cluster State)
# =====================================================================
async def get_database_connection_pool():
    """Simulates an asynchronous database connection lease context."""
    # Imagine claiming a real socket from an asyncpg connection pool here
    await asyncio.sleep(0.05) 
    yield "ACTIVE_POOL_SOCKET_REF_8821"
    # Code after the yield acts as a teardown phase when the request finishes

# =====================================================================
# PROJECT PATH A: THE ASYNC REST API
# =====================================================================
@app.get("/api/v1/compute-metrics")
async def fetch_cluster_metrics(
    node_id: str, 
    db_socket: str = Depends(get_database_connection_pool)
):
    """
    Handles incoming HTTP GET traffic using a non-blocking timeline.
    Thousands of users can query this endpoint simultaneously.
    """
    start_time = time.time()
    print(f"[HTTP Router] Request received for node: {node_id} | Using socket: {db_socket}")
    
    # Simulate a non-blocking external network/database read
    await asyncio.sleep(1.0)
    
    processing_window = time.time() - start_time
    return {
        "status": "SUCCESS",
        "node_id": node_id,
        "execution_window_seconds": f"{processing_window:.4f}",
        "payload": {"cpu_utilization": 42.5, "active_threads": 1}
    }

# =====================================================================
# PROJECT PATH B: THE REAL-TIME WEBSOCKET HUB
# =====================================================================
class ConnectionManager:
    """Manages long-lived persistent WebSocket sockets on our single thread."""
    def __init__(self):
        self.active_sockets: set[WebSocket] = set()

    async def connect(self, websocket: WebSocket):
        await websocket.accept()
        self.active_sockets.add(websocket)
        print(f"[WebSocket Hub] 🔌 New persistent live stream connected. Total: {len(self.active_sockets)}")

    def disconnect(self, websocket: WebSocket):
        self.active_sockets.discard(websocket)
        print(f"[WebSocket Hub] 🔴 Socket dropped. Active connections left: {len(self.active_sockets)}")

    async def broadcast_telemetry(self, raw_text: str):
        """Fans out a broadcast message across all open live channels."""
        if not self.active_sockets:
            return
            
        print(f"[WebSocket Hub] Broadcasting chunk: '{raw_text}' to {len(self.active_sockets)} clients...")
        payload = {"timestamp": time.time(), "broadcast_message": raw_text}
        
        # Distribute updates concurrently across all connections
        tasks = [asyncio.create_task(ws.send_json(payload)) for ws in self.active_sockets]
        await asyncio.gather(*tasks, return_exceptions=True)

socket_broker = ConnectionManager()

@app.websocket("/ws/telemetry-stream")
async def live_telemetry_endpoint(websocket: WebSocket):
    """
    Maintains a persistent, stateful, bi-directional network pipe.
    The Event Loop manages this socket indefinitely without thread thrashing.
    """
    await socket_broker.connect(websocket)
    try:
        while True:
            # Suspension Point: Free the thread until this client sends a packet
            incoming_bytes = await websocket.receive_text()
            print(f"[WebSocket Received]: '{incoming_bytes}'")
            
            # Broadcast the received message out to all other connected clients
            await socket_broker.broadcast_telemetry(incoming_bytes)
            
    except WebSocketDisconnect:
        socket_broker.disconnect(websocket)
    except Exception as err:
        print(f"[WebSocket Exception] Isolated error: {err}")
        socket_broker.disconnect(websocket)

# =====================================================================
# BACKGROUND RECURSIVE METRICS EMITTER
# =====================================================================
@app.on_event("startup")
async def launch_background_heartbeat_loop():
    """Spawns an independent, infinite background task to emit metrics."""
    async def heartbeat_ticker():
        while True:
            await asyncio.sleep(5.0) # Emit an update every 5 seconds
            await socket_broker.broadcast_telemetry("SYSTEM_HEARTBEAT_TICK_OK")
            
    asyncio.create_task(heartbeat_ticker())