'''
Mutable vs Immutable Data Types
'''

# 1. Immutable Example (String)
chef_name = "Chef Ranveer"
print(f"Initial Name: {chef_name} | ID: {id(chef_name)}")

# We "add" to the string
chef_name = chef_name + " Brar"
print(f"Updated Name: {chef_name} | ID: {id(chef_name)}")

print("-" * 40)

# 2. Mutable Example (Your Set)
spice_mix = set()
print(f"Initial Mix : {spice_mix}       | ID: {id(spice_mix)}")

# We add to the set
spice_mix.add("Ginger")
print(f"Updated Mix : {spice_mix} | ID: {id(spice_mix)}")