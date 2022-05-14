def print_name_local():
    first_name = "Taro"
    last_name = "Yamada"
    print(first_name, last_name)


print_name_local()
# print(first_name)  # ローカル変数

age = 30

def print_age():
    global age
    age = 20
    print(age)

print(age)
print_age()
print(age)