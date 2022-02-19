fruits = ["apple", "peach", "melon", "grapes"]
# print(fruits)
# print(fruits[0])
# print(fruits[-1])
# print("hello world"[3])

fruits.append("orange")
print(fruits)

fruits.insert(2,"banana")
print(fruits)

fruits.remove("peach")
print(fruits)

fruits.sort()
print((fruits))

fruits.sort(reverse=True)
print((fruits))

print(len(fruits))