#yeild can also receive values from the caller using the send() method. The value sent will be the result of the yield expression.

def chai_customer():
    print("Welcome ! What chai would you like ?")
    order = yield  # this is primint the generator so it will wait for the first send() to provide the order
    while True:
        print(f"Preparing: {order}")
        order = yield

stall = chai_customer()
# print(next(stall)) # first yeild results to none
next(stall)     # priming the generator

for tea in ["Masala Chai", "Lemon Chai", "Ginger Chai", 'ulong Chai']:
    stall.send(tea)  # sending the order to the generator
    # next(stall)  # dont do this 

