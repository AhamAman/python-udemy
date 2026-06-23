#mro -  c3 linearisation method resolution order

class A:
    label = "A: Base class"

class B(A):
    label = "B: Masala blend"

class C(A):
    label = "C: Herbal blend"

class D(C, B):
    pass

cup = D()

#C takes precedence over B because of the order of inheritance in D (C, B) and the mro method resolution order
print(cup.label)
print(D.__mro__)