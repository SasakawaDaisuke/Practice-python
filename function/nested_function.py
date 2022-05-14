msg = "global"

def outer():
    # global msg
    msg = "outer"

    def inner():
        nonlocal msg
        msg = "inner"
        print("This is inner function")
    inner()

outer()
print(msg)