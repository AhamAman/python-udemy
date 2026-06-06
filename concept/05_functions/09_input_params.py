'''
Passed functions and mutbility of data types
'''

# chai = "Ginger chai"

# def prepare_chai(order):
#     print("Preparing ", order)


# prepare_chai(chai)
# print(chai)


# pass by object reference
chai = [1, 2, 3]

def edit_chai(cup):
    cup[1] = 42

edit_chai(chai)
print(chai)


#positional and keyword arguments
def make_chai(tea, milk, sugar):
    print(tea, milk, sugar)

make_chai("Darjeeling", "Yes", "Low") #positional
make_chai(tea="Green", sugar="Medium", milk="No") #keywords


#arbitary number of arguments
def special_chai(*ingredients, **extras):
    print("Ingredients", ingredients)
    print("Extras", extras)

special_chai("Cinnamon", "Cardmom", sweetener="Honey", foam="yes")

'''
The default trap
'''

# def chai_order(order=[]):
#     order.append("Masala")
#     print(order)

def chai_order(order=None):
    if order is None:
        order = []
    print(order)

chai_order()
chai_order()