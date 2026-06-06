device_status = "active"
temperature = 38
'''
nested if statements - if statement inside another if statement 
one needs to be true for the other to be checked'''

if device_status == "active":
    if temperature > 35:
        print("High temperature alert!")
    else:
        print("Temperature is normal")
else:
    print("Device is offline")