# Raw dataset: Messy, duplicate audit log entries from a cluster server network
RAW_SECURITY_LOGS = [
    {"user": "alice", "action": "LOGIN",  "ip": "10.0.0.5"},
    {"user": "bob",   "action": "UPDATE", "ip": "10.0.0.9"},
    {"user": "alice", "action": "LOGIN",  "ip": "10.0.0.5"}, # Duplicate entry
    {"user": "charlie","action": "DELETE", "ip": "10.0.0.2"},
    {"user": "bob",   "action": "UPDATE", "ip": "10.0.0.9"}, # Duplicate entry
]

# ==========================================
# 1. Inline Data Deduplication
# ==========================================
print("--- 1. Data Deduplication Phase ---")

# Target: Extract a clean array of all unique user names who interacted with the system
# The set comprehension automatically drops redundant entries
unique_users = {log["user"] for log in RAW_SECURITY_LOGS}

print(f"Original Log Count: {len(RAW_SECURITY_LOGS)}")
print(f"Deduplicated Users Set: {unique_users} | Type: {type(unique_users)}")


# ==========================================
# 2. Conditional Set Creation
# ==========================================
print("\n--- 2. Conditional Set Creation ---")

# Target: Identify unique IPs that were used for critical administrative modifications ("UPDATE" or "DELETE")
admin_ips = {
    log["ip"] 
    for log in RAW_SECURITY_LOGS 
    if log["action"] in {"UPDATE", "DELETE"}
}
print(f"Flagged Admin IP Manifest: {admin_ips}")


# ==========================================
# 3. Membership Optimization Use Case
# ==========================================
print("\n--- 3. O(1) Membership Lookup Strategy ---")

# A massive list of banned, malicious IP addresses (simulated scale)
BANNED_IP_LIST = ["192.168.1.1", "10.0.0.9", "172.16.0.4", "10.0.0.9"]

# Optimization Step: Convert the slow linear list into a lightning-fast hash map set
banned_ip_lookup_pool = {ip for ip in BANNED_IP_LIST}

# Live packet stream check
incoming_packet_ip = "10.0.0.9"

# This evaluation runs instantly at O(1) velocity because it uses set hashing mechanics
if incoming_packet_ip in banned_ip_lookup_pool:
    print(f"[ALERT] Connection from {incoming_packet_ip} dropped instantly by firewall gate.")