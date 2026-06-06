#dictionaries

#way 1
chai_order = dict(type="Masala Chai", size="Large", sugar=2)
print(f"Chai order: {chai_order}")

#way 2 to create a dictionary
chai_recipe = {}
chai_recipe["base"] = "black tea"
chai_recipe["liquid"] = "milk"
# print(f"Chai recipe: {chai_recipe}")

print(f"Recipe base: {chai_recipe['base']}")
print(f"Recipe: {chai_recipe}")

#deleting a key-value pair from a dictionary
del chai_recipe["liquid"]
print(f"Recipe: {chai_recipe}")

print(f"Is sugar in the order? {'sugar' in chai_order}")

chai_order = {"type": "Ginger Chai", "size": "Medium", "sugar": 1}

# print(f"Order details (keys): {chai_order.keys()}")
# print(f"Order details (values): {chai_order.values()}")
# print(f"Order details (items): {chai_order.items()}")

# popitem() removes and returns the last inserted key-value pair as a tuple
last_item = chai_order.popitem()
print(f"Removed last item: {last_item}")

#updating a dictionary with another dictionary
extra_spices = {"cardamom": "crushed", "ginger": "sliced"}
chai_recipe.update(extra_spices)

print(f"Updated chai recipe: {chai_recipe}")

#safe way to access a value from a dictionary using get() method
customer_note = chai_order.get("size", "NO Note")
print(f"customer_note is: {customer_note}")