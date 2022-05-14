# *args
print("hello", "world", "test")
def get_average(*args):
    num = len(args)
    if num == 0:
        return 0
    total = sum(args)
    return total/num

average = get_average(1, 2, 3, 4, 5)
print(average)

# **kwargs；ディクショナリー形式で受け取る
def kwargs_func(**kwargs):
    param1 = kwargs.get("param1", 1)
    param2 = kwargs.get("param2", 2)
    param3 = kwargs.get("param3", 3)

    print(kwargs)


kwargs_func(param1=10, param2=6, param3=100)