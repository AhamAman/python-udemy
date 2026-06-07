# Generator function stalls the function so we can have potentially infinite number of yields. We can use next() to get the next value from the generator.

def infinite_chai():
    count = 1
    while True:
        yield f"Refil #{count}"  # yeild doesnt stops the functioon - the stack frame is not gone
        count += 1

refill = infinite_chai()
user2 = infinite_chai()

for _ in range(5):
    print(next(refill))

for _ in range(6):
    print(next(user2))