import asyncio
import time
import asyncpg

# Database Connection Details String (DSN)
# Format: postgresql://user:password@host:port/database_name
DB_DSN = "postgresql://postgres:postgres@127.0.0.1:5432/postgres"

async def init_database_schema(pool):
    """Acquires a connection from the pool to set up baseline relational tables."""
    async with pool.acquire() as conn:
        print("[Database] Creating operational table grids...")
        await conn.execute("""
            CREATE TABLE IF NOT EXISTS product_inventory (
                product_id SERIAL PRIMARY KEY,
                product_name TEXT NOT NULL,
                price_cents INTEGER NOT NULL,
                stock_count INTEGER NOT NULL
            );
        """)
        # Clear out any residual data from previous runs
        await conn.execute("TRUNCATE TABLE product_inventory;")

# =====================================================================
# THE CRUD INTERFACE COMPONENT LAYER
# =====================================================================

async def create_product(pool, name, price, stock):
    """INSERT Operation: Adds a record and returns the auto-generated primary key ID."""
    async with pool.acquire() as conn:
        # Talks directly to Postgres binary protocol using structured variables ($1, $2)
        row = await conn.fetchrow("""
            INSERT INTO product_inventory (product_name, price_cents, stock_count)
            VALUES ($1, $2, $3) RETURNING product_id;
        """, name, price, stock)
        return row['product_id']

async def read_product_by_id(pool, product_id):
    """SELECT Operation: Fetches a specific row dictionary by ID."""
    async with pool.acquire() as conn:
        row = await conn.fetchrow(
            "SELECT * FROM product_inventory WHERE product_id = $1;", 
            product_id
        )
        return dict(row) if row else None

async def update_stock_atomic(pool, product_id, quantity_change):
    """UPDATE Operation: Wraps execution inside an atomic transaction block."""
    async with pool.acquire() as conn:
        # Open a secure transaction boundary
        async with conn.transaction():
            # Check current inventory levels securely
            current_stock = await conn.fetchval(
                "SELECT stock_count FROM product_inventory WHERE product_id = $1 FOR UPDATE;",
                product_id
            )
            
            if current_stock + quantity_change < 0:
                raise ValueError(f"Transaction aborted: Insufficient stock for product #{product_id}.")
                
            await conn.execute("""
                UPDATE product_inventory 
                SET stock_count = stock_count + $1 
                WHERE product_id = $2;
            """, quantity_change, product_id)

async def delete_product(pool, product_id):
    """DELETE Operation: Permanently drops a record by ID mapping."""
    async with pool.acquire() as conn:
        await conn.execute("DELETE FROM product_inventory WHERE product_id = $1;", product_id)


# =====================================================================
# CONCURRENT EXECUTION MATRIX RUNTIME
# =====================================================================

async def main():
    print("=== INITIALIZING ACCELERATED ASYNC DATABASE POOL ===")
    start_time = time.time()
    
    # 1. Start the persistent, asynchronous connection pool container
    # Sets up 5 reusable persistent socket pipes to our PostgreSQL instance
    async with asyncpg.create_pool(dsn=DB_DSN, min_size=2, max_size=5) as db_pool:
        
        # Initialize schema tables
        await init_database_schema(db_pool)
        
        # 2. RUN CONCURRENT CRUD WRITE INJECTIONS (Fan-Out)
        print("\n[Main] Injecting inventory records concurrently using the pool...")
        products_to_insert = [
            ("Quantum Laptop Engine", 149900, 10),
            ("Mechanical Macro Keyboard", 12500, 50),
            ("OLED Spatial Monitor", 89900, 15),
            ("Titanium Ergo Desk", 65000, 5)
        ]
        
        insert_tasks = [
            asyncio.create_task(create_product(db_pool, name, p, s))
            for name, p, s in products_to_insert
        ]
        
        # Capture generated primary IDs simultaneously
        generated_ids = await asyncio.gather(*insert_tasks)
        print(f"[Main] Insertion successful. Created Record IDs: {generated_ids}")
        
        # 3. CONCURRENT STOCK MODIFICATIONS
        print("\n[Main] Processing stock modifications concurrently across transaction blocks...")
        target_product = generated_ids[0] # Let's target the Quantum Laptop Engine
        
        # Attempt three sales and one return concurrently
        stock_tasks = [
            asyncio.create_task(update_stock_atomic(db_pool, target_product, -2)), # Purchase 2
            asyncio.create_task(update_stock_atomic(db_pool, target_product, -1)), # Purchase 1
            asyncio.create_task(update_stock_atomic(db_pool, target_product, 5)),  # Restock 5
            asyncio.create_task(update_stock_atomic(db_pool, target_product, -3))  # Purchase 3
        ]
        
        await asyncio.gather(*stock_tasks)
        
        # 4. FETCH FINAL AUDIT RECEIPT
        print("\n[Main] Fetching updated data receipt record...")
        final_record = await read_product_by_id(db_pool, target_product)
        print(f"📄 [Final Inventory State for Product #{target_product}]:")
        print(f"   Name:  {final_record['product_name']}")
        print(f"   Price: ${final_record['price_cents'] / 100:.2f}")
        print(f"   Stock: {final_record['stock_count']} units remaining")
        
        # 5. CLEAN UP TEST ENVIRONMENT
        print("\n[Main] Purging record tables...")
        await delete_product(db_pool, target_product)
        
    print(f"\nAll operations completed. Runtime engine closed in {time.time() - start_time:.2f} seconds.")

if __name__ == "__main__":
    # Ensure postgres database server is up and running before booting script
    try:
        asyncio.run(main())
    except Exception as e:
        print(f"\n🚨 System Configuration Failure: {e}")