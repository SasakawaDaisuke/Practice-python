# forループ
fruits = ["apple", "peach", "melon", "grapes"]

# for fruit in fruits:
#     print(fruit)

# for char in "Hello World!!":
#    print(char)

# for i in range(-2, 6, 2):
#     print(i)

# for _ in range(-2, 6, 2):
#     print("a")

for i in range(1,51):
    if i % 15 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)