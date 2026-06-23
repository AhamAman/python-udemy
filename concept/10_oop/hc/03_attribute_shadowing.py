'''
Class namespace vs Instance namespace
'''

class Chai:
    temperature = "hot"
    strength = "Strong"

#looks into the class namespace and finds the attribute and not instance namespace namespace
cutting = Chai()
print(cutting.temperature)

cutting.temperature = "Mild"
cutting.cup = "small"

# now we look directly into the instance namespace and finds the attribute
print("After changing ",cutting.temperature)
print("cup size is  ",cutting.cup)
print("Direct look into the class ", Chai.temperature)

del cutting.temperature
del cutting.cup

# now this is attribuute error because we have deleted the attribute from instance namespace and class namespace does not have this attribute
print(cutting.temperature)
print(cutting.cup)