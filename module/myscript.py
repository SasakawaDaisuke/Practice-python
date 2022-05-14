import sys
sys.path.append("/Users/sasakawa/Desktop/Udemy/practice-python/function")
import mymodule
import scope

mymodule.myfunc()
print(mymodule.myvariable)

print(sys.path)

scope.print_name_local()