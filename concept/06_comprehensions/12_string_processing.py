# Raw un-sanitized log string buffer segment containing noise metadata
RAW_ERROR_DATA = "ERR_V2::[auth-fail]::id-9081__token=A9x7_Q"

# ==========================================
# 1. Character-Level Filtering & Transformation
# ==========================================
print("--- 1. Character Extraction and Casing ---")

# Task: Extract ONLY the alphabetic letters from the raw text string, 
# completely throwing away numbers, underscores, brackets, and colons.
# We simultaneously normalize all extracted characters to lowercase.
clean_letters_array = [char.lower() for char in RAW_ERROR_DATA if char.isalpha()]

# Join the array back together into a clean, uniform string sequence
normalized_text = "".join(clean_letters_array)
print(f"Original Buffer: {RAW_ERROR_DATA}")
print(f"Sanitized Text:  {normalized_text}")


# ==========================================
# 2. Tokenization and Parsing Fields
# ==========================================
print("\n--- 2. Parsing Tokens and API Payloads ---")

RAW_CSV_ROW = "  node-us-east ; ONLINE ;  cpu=45% ; mem=12Gb  "

# Task: Parse the semi-colon delimited string row into a clean token list.
# 1. Split the string by the delimiter ';' (yields raw split substring pieces).
# 2. Iterate through those substrings, stripping out empty trailing margins.
# 3. Transform the tokens to completely uppercase structures.
sanitized_tokens = [token.strip().upper() for token in RAW_CSV_ROW.split(";")]
print(f"Raw Entry Array: {RAW_CSV_ROW.strip()}")
print(f"Parsed Tokens:   {sanitized_tokens}")


# ==========================================
# 3. Targeted Strategic Feature Extraction
# ==========================================
print("\n--- 3. Extracting Key-Value Features ---")

# Complex input sample representing a collection of configuration flags
CONFIG_STRING = "debug=true,verbose=false,cache=true,log_level=info"

# Task: Turn this comma-separated string into a clean associative dictionary map.
# Step A: Split by ',' to get ['debug=true', 'verbose=false', ...]
# Step B: Deploy a Dictionary Comprehension to split each pair on '=' inline.
config_map = {
    pair.split("=")[0]: pair.split("=")[1]
    for pair in CONFIG_STRING.split(",")
}

print(f"Parsed Config Map Dictionary:\n  {config_map}")
print(f"Direct Lookup 'log_level' -> {config_map['log_level']}")