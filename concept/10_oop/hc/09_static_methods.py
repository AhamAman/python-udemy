'''
Not a instance method, not a class method, but a static method. Static methods are defined using the @staticmethod decorator and do not take the instance (self) or class (cls) as the first argument. They are like regular functions that belong to a class's namespace
'''

class ChaiUtils:
    @staticmethod
    def clean_ingredients(text):
        return [item.strip() for item in text.split(",")]
    

raw = " water , milk , ginger , honey "

cleaned = ChaiUtils.clean_ingredients(raw)
print(cleaned)