# 参照渡し(aのアドレスが関数内と同じものかどうか)
def add_nums(a, b):
    print(id(a))
    return a + b


one = 1
two = 2
print(id(one))
print(add_nums(one, two))