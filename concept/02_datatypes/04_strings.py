# ==========================================
# 1. Creation and Quote Mechanics
# ==========================================
print("--- String Creation ---")
single = 'Single quotes allow "double" quotes inside'
double = "Double quotes allow 'single' quotes inside"
multiline = """This is a triple-quoted string.
It preserves newlines
and formatting."""

print(single)
print(multiline)

# ==========================================
# 2. Indexing and Slicing (The Coordinate System)
# ==========================================
print("\n--- Indexing and Slicing ---")
#  P  y  t  h  o  n
#  0  1  2  3  4  5
# -6 -5 -4 -3 -2 -1
lang = "Python"

print(f"First character (lang[0]): {lang[0]}")
print(f"Last character (lang[-1]): {lang[-1]}")

# Slicing: [start:stop] -> stop is exclusive (up to, but not including)
print(f"Slice [0:2]: {lang[0:2]}")   # "Py"
print(f"Slice [2:]:  {lang[2:]}")    # "thon" (from index 2 to end)
print(f"Reverse string [::-1]: {lang[::-1]}") # "nohtyP"

# ==========================================
# 3. Immutability & Manipulations
# ==========================================
print("\n--- Immutability & Manipulation ---")
word = "cat"
print(f"Original object ID: {id(word)}")

try:
    word[0] = "b"  # This will fail! You cannot mutate a string.
except TypeError as error:
    print(f"Caught Error: {error}")

# Concatenation (+) and Repetition (*) create NEW strings
new_word = "bat" + "man"
replicated = "Yo! " * 3
print(f"Concatenation: {new_word} | Repetition: {replicated}")

# Common methods (all return completely new string objects)
mixed_str = "   pYtHoN   "
print(f"Cleaned up: '{mixed_str.strip().capitalize()}'")

# ==========================================
# 4. Unicode & Encoding/Decoding
# ==========================================
print("\n--- Encoding & Decoding ---")
# Unicode support out of the box
emoji_text = "Hello 🐍" 
print(f"Unicode String: {emoji_text} | Length: {len(emoji_text)}")

# Transform text object into a stream of raw binary bytes (Encoding)
binary_data = emoji_text.encode('utf-8')
print(f"Encoded to Bytes: {binary_data} | Type: {type(binary_data)}")

# Transform raw binary bytes back into a text object (Decoding)
decoded_text = binary_data.decode('utf-8')
print(f"Decoded back to String: {decoded_text}")