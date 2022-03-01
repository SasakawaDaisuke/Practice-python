myvariable = "This is global variable!!"


def myfunc():
    print("This is my func!!")

def _anotherfunc():
    print("This is another func!!")

if __name__ == "__main__":
    myfunc()
    _anotherfunc()
    print(myvariable)
    print("This is my module!!")