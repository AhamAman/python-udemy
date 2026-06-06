'''
Handling return values from functions
'''
# def make_chai():
#     # return "Here is your masal chai"
#     print("Here is your masala chai")

# return_value = make_chai()

# print(return_value)

def idle_chaiwala():
    pass

#pass prints none
print(idle_chaiwala())

def sold_cups():
    return 120

#function call is an expression that evaluates to the return value of the function
total = sold_cups()
print(total)

# return + conditionals jazz
def chai_status(cups_left):
    if cups_left == 0:
        return "Sorry, chai over"
    return "Chai is ready"
    

print(chai_status(0))
print(chai_status(5))

#handling multiple return values
def chai_report():
    return 100, 20, 10 # sold, remaining

sold, remaining, not_paid = chai_report()
print("Sold: ", sold)
print("Remaining: ", remaining)