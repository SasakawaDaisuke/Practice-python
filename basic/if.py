# if文

age = 27
age_alcohol = 20
age_drive =18

if age >= age_alcohol:
    print(" You can drink!!")
elif age >= age_drive:
    print("You can not drive!!")
else:
    print("You can not drink!!")

balance = 1000
withdraw = 100
withdraw_limit = 1000000

if withdraw >= withdraw_limit:
    print("引き出し額の上限は100万円です。")
elif balance >= withdraw:
    balance -= withdraw
    print(f"残高は：{balance}円です。")
else:
    print("残高が足りません")
