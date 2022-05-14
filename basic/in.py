fruits = ["apple", "peach", "melon", "grapes"]
# print("apple" in fruits)
# print("lemon" not in fruits)

favorite_fruit = input("好きなフルーツはなんですか？")

if favorite_fruit in fruits:
    print("差し上げます")
    fruits.remove(favorite_fruit)
    print(fruits)
else:
    print("入荷しておきます")
    fruits.append(favorite_fruit)
    print(fruits)
