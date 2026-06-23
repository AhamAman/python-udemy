"""
PYTHON GENERATOR DEMO: COOPERATIVE MULTITASKING & STATE MANIPULATION

Mental Model:
Caller (Main Thread) <========================> Generator (State Machine)
next(gen)            ------------> Starts / Resumes
gen.send(value)      ------------> Injects value into the paused `yield`
gen.throw(error)     ------------> Injects error into the paused `yield`
gen.close()          ------------> Raises GeneratorExit to forcefully terminate
"""

def interactive_generator():
    print("\n[Gen] 🎬 Engine started. Running until first yield...")
    
    try:
        # 1. Yields out a value, pauses, and waits for input to replace this expression.
        input_a = yield "Yield 1: Please send Input A"
        print(f"[Gen] 📥 Received Input A: '{input_a}'")
        
        # 2. Yields another value, pauses, and waits for the next input.
        input_b = yield "Yield 2: Please send Input B"
        print(f"[Gen] 📥 Received Input B: '{input_b}'")
        
    except ValueError as error:
        # 3. Catches errors injected from the outside via gen.throw()
        print(f"[Gen] 💥 Caught external emergency: '{error}'")
        yield "Yield 3 (Recovery): Handling error, standing by..."
        
    except GeneratorExit:
        # 4. Caught specifically when gen.close() is called from the outside
        print("[Gen] 🛑 Received force-close signal via GeneratorExit!")
        raise # Must re-raise GeneratorExit (or let it propagate) to successfully close
        
    finally:
        # 5. Always executes when the generator terminates or is closed
        print("[Gen] 🧹 Cleanup: Running finally block to free resources.")

    return "🏁 Execution Finished Automatically"


# ============================================================================
# EXECUTION LINE-BY-LINE
# ============================================================================

if __name__ == "__main__":
    print("--- 1. Initialization ---")
    gen = interactive_generator() # State: Created but not started.

    print("\n--- 2. First next() (Kickstart) ---")
    # We prime the generator. We cannot use send(value) yet because it hasn't paused at a yield.
    step1 = next(gen)
    print(f"👉 Caller received: '{step1}'")

    print("\n--- 3. Second Step: gen.send(value) ---")
    # 'Data X' physically replaces the `yield "Yield 1..."` expression inside the generator.
    step2 = gen.send("Data X")
    print(f"👉 Caller received: '{step2}'")

    print("\n--- 4. Third Step: gen.throw(exception) ---")
    # Instead of data, we fire an exception directly into the generator's current pause point.
    step3 = gen.throw(ValueError("Network Timeout!"))
    print(f"👉 Caller received after throw: '{step3}'")

    print("\n--- 5. Fourth Step: gen.close() (Abrupt Termination) ---")
    # gen.close() injects a GeneratorExit exception at the current yield point.
    # It forces the generator into its GeneratorExit catch block and finally block, then exits.
    try:
        gen.close()
        print("👉 Generator successfully closed.")
    except StopIteration:
        pass

    print("\n--- 6. Post-Close Behaviour ---")
    # Once a generator is closed or completed, calling next() on it raises StopIteration.
    try:
        next(gen)
    except StopIteration:
        print("👉 Caller tried to advance, but generator is dead (StopIteration caught).")

