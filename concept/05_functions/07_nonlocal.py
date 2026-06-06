
chai_type = "ginger"
#nonlocal is to access the variable of the outer function in the inner function
def update_order():
    chai_type = "Elaichi"
    def kitchen():
        nonlocal chai_type
        chai_type = "Kesar"
    kitchen()
    print("After kitchen update", chai_type)

update_order()