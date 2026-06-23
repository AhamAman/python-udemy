import asyncio
import time
from typing import Dict, List
from pydantic import BaseModel, Field
from fastapi import FastAPI, Depends, WebSocket, WebSocketDisconnect, HTTPException, status

app = FastAPI(
    title="Accelerated Financial Processing Engine",
    description="High-Throughput ASGI Dual-Protocol Matrix Layer."
)

# =====================================================================
# DATA SCHEMA AND RECORD INVENTORY LAYER
# =====================================================================
class OrderModel(BaseModel):
    ticker: str = Field(..., min_length=1, max_length=5, examples=["AAPL"])
    quantity: int = Field(..., gt=0, description="Volume must be positive")
    price_cents: int = Field(..., gt=0, description="Price must be greater than zero")

# In-memory transaction data ledger
transaction_lake: List[Dict] = []


# =====================================================================
# ASYNC DEPENDENCY INJECTION LAYER (Security Guardrail)
# =====================================================================
async def verify_api_routing_token(client_token: str = "DEFAULT_TOKEN_8821"):
    """
    Simulates an asynchronous authentication check.
    Fetches keys via non-blocking network streams before resolving the route.
    """
    # Non-blocking yield to let the loop process background traffic during authentication
    await asyncio.sleep(0.02)
    if not client_token.startswith("DEFAULT_TOKEN"):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, 
            detail="Invalid cryptographic authorization routing signature."
        )
    return f"Authenticated-Context-{int(time.time())}"


# =====================================================================
# REAL-TIME WEBSOCKET CHANNELS BROKER
# =====================================================================
class LiveLedgerBroker:
    """Manages high-volume persistent streaming socket matrices on a single thread."""
    def __init__(self):
        self.active_sockets: set[WebSocket] = set()

    async def register_node(self, websocket: WebSocket):
        await websocket.accept()
        self.active_sockets.add(websocket)
        print(f"[WebSocket Hub] 🔌 New streaming node bound. Active pool: {len(self.active_sockets)}")

    def unregister_node(self, websocket: WebSocket):
        self.active_sockets.discard(websocket)
        print(f"[WebSocket Hub] 🔴 Node dropped. Remaining pool: {len(self.active_sockets)}")

    async def broadcast_order_receipt(self, payload: dict):
        """Fans-out execution payloads concurrently across all active channels."""
        if not self.active_sockets:
            return
            
        # Transform payload to task array for true concurrent dispatching
        tasks = [asyncio.create_task(ws.send_json(payload)) for ws in self.active_sockets]
        # Gather executes them concurrently on the loop
        await asyncio.gather(*tasks, return_exceptions=True)

# Global singleton broadcast broker
live_ledger = LiveLedgerBroker()


# =====================================================================
# PROJECT PATH A: THE ASYNC REST ENDPOINT (Order Ingestion)
# =====================================================================
@app.post("/api/v1/order/ingest", status_code=status.HTTP_201_CREATED)
async def ingest_market_order(
    order: OrderModel,
    auth_ctx: str = Depends(verify_api_routing_token)
):
    """
    Asynchronous REST Ingestion Gateway.
    Accepts incoming financial transactions, validates parameters via Pydantic,
    appends to ledger data structures, and triggers live broadcast streams.
    """
    start_time = time.time()
    order_id = f"ORD-{len(transaction_lake) + 1001}"
    
    # Simulate a non-blocking database write latency overhead
    await asyncio.sleep(0.1)
    
    order_payload = {
        "order_id": order_id,
        "ticker": order.ticker.upper(),
        "volume": order.quantity,
        "value_usd": f"${(order.price_cents * order.quantity) / 100:.2f}",
        "auth_signature": auth_ctx,
        "processed_at": time.time()
    }
    
    # Commit to our localized record matrix
    transaction_lake.append(order_payload)
    
    # Trigger non-blocking WebSocket fan-out broadcast notification
    await live_ledger.broadcast_order_receipt({
        "event_type": "ORDER_EXECUTED",
        "data": order_payload
    })
    
    return {
        "status": "ACCEPTED",
        "order_id": order_id,
        "ingest_latency_ms": f"{(time.time() - start_time) * 1000:.2f}"
    }


# =====================================================================
# PROJECT PATH B: THE REAL-TIME WEBSOCKET ENDPOINT (Streaming Ledger)
# =====================================================================
@app.websocket("/ws/live-ticker")
async def live_ticker_feed(websocket: WebSocket):
    """
    Stateful real-time data streaming route.
    Maintains a long-lived persistent TCP handshake window open on the single thread.
    """
    await live_ledger.register_node(websocket)
    try:
        while True:
            # SUSPENSION POINT: Yields thread entirely until this client sends a text frame
            incoming_raw_text = await websocket.receive_text()
            print(f"[WebSocket Echo Packet]: Received raw token -> '{incoming_raw_text}'")
            
            # Simple bi-directional heartbeat check command loop
            if incoming_raw_text.upper() == "PING":
                await websocket.send_text("PONG")
                
    except WebSocketDisconnect:
        live_ledger.unregister_node(websocket)
    except Exception as err:
        print(f"[WebSocket System Exception] Fault isolated on socket: {err}")
        live_ledger.unregister_node(websocket)


# =====================================================================
# SYSTEM LEVEL STARTUP BACKGROUND TRACK TICKER
# =====================================================================
@app.on_event("startup")
async def launch_background_market_ticker():
    """Spawns an independent infinite task to push system ticks down streams."""
    async def market_feed_simulator():
        tick_count = 0
        while True:
            await asyncio.sleep(3.0) # Generate data every 3 seconds
            tick_count += 1
            await live_ledger.broadcast_order_receipt({
                "event_type": "MARKET_TICK",
                "tick_id": tick_count,
                "timestamp": time.time(),
                "status": "HEALTHY_MATRIX"
            })
            
    asyncio.create_task(market_feed_simulator())