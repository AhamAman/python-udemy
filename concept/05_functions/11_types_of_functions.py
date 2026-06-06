# pure and impure functions
def pure_chai(cups):
    return cups * 10

total_chai = 0

# not recommended cause play with global variable
def impure_chai(cups):
    global total_chai
    total_chai += cups

# recursive function see problem broken to smaller versions of itself and see exit way as well
def pour_chai(n):
    print(n)
    if n == 0:
        return "All cups poured"
    return pour_chai(n-1)

print(pour_chai(3))


#lambda function and use in filter function
chai_types = ["light", "kadak", "ginger", "kadak"]

#filter need both condiiton and iterable and return a filter object which is an iterator that can be converted to list or set or tuple
strong_chai = list(filter(lambda chai: chai!="kadak", chai_types))

print(strong_chai)