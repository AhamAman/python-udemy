class TeaLeaf:
    def __init__(self, age):
        self._age = age #_age means it is a private variable, it should not be accessed directly outside the class. We will use property decorators to control access to this variable.

    @property
    def age(self):   #convert standard function to getter attribute
        return self._age + 2
    
    @age.setter
    def age(self, age):
        if 1 <= age <= 5:
            self._age = age
        else:
            raise ValueError("Tea leaf age must be between 1 and 5 years")
        
leaf = TeaLeaf(2) # getter take private variable and add 2 to it, so it will return 4 when we call leaf.age
print(leaf.age)

leaf.age = 6 # this checks for setter and raises an error because 6 is not between 1 and 5
print(leaf.age)
