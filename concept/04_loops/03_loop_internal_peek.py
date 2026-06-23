# =====================================================================
# DEMO: MANUALLY REPLICATING A FOR LOOP VIA THE ITERATOR PROTOCOL
# =====================================================================

# 1. Define our Iterable (The Warehouse)
shopping_list = ["eggs", "milk", "bread"]

print("--- Step 1: Checking Types ---")
print(f"Is shopping_list an iterable? Yes, it has __iter__: {hasattr(shopping_list, '__iter__')}")
print(f"Does shopping_list have __next__? {hasattr(shopping_list, '__next__')} (No, it needs an iterator)")

# 2. Convert the Iterable into an Iterator (The Bookmark)
# This is exactly what Python does when a 'for' loop begins.
list_iterator = iter(shopping_list)

print("\n--- Step 2: Checking the Iterator ---")
print(f"Does the iterator have __next__? {hasattr(list_iterator, '__next__')} (Yes! It can fetch items)")

# 3. Manually fetching items using next()
print("\n--- Step 3: Manually driving the iterator ---")
print("First call:", next(list_iterator))
print("Second call:", next(list_iterator))
print("Third call:", next(list_iterator))

# 4. What happens if we call next() again when it's empty?
print("\n--- Step 4: Triggering the End Condition ---")
try:
    print("Fourth call...")
    next(list_iterator)  # This will fail because the list is empty
except StopIteration:
    print("Caught a 'StopIteration' exception! The iterator is completely exhausted.")


print("\n--- Step 5: Simulating a Complete 'For' Loop Manually ---")
# Resetting the iterator because the previous one was exhausted
fresh_iterator = iter(shopping_list)

# This infinite while loop behaves EXACTLY like a Python 'for' loop
while True:
    try:
        # Get the next item
        item = next(fresh_iterator)
        # Execute the loop body
        print(f"Loop Body Processing: {item}")
    except StopIteration:
        # If StopIteration is raised, break the loop cleanly
        print("StopIteration caught! Exiting loop cleanly.")
        break

print("\nDemo complete!")