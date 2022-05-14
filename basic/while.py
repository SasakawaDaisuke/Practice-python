# while文

# count = 0
# while count < 10:
#     print(count)
#     count += 1

# while True:
#     age = int(input("あなたは何歳ですか？"))
#     if not 0 <= age <= 120:
#         print("入力された値は正しくありません。")
#         continue
#     else:
#         print(f"あなたは{age}歳です")
#         break
#
# # input():ユーザーが入力した値を取得する

age_casino = 18
game_dict = {"1": "ルーレット", "2": "ブラックジャック", "3": "ポーカー"}

while True:
    age = int(input("何歳ですか:"))
    if not 0 <= age <= 120:
        print("入力された値は正しくありません。")
        continue
    elif age >= age_casino:
        print("カジノにようこそ")
        print("どのゲームで遊びますか？")
        break
    else:
        print("18歳未満は入場できません")
        break


while True:
    game = input(game_dict)
    if game in game_dict:
        print(f"あなたは{game_dict[game]}を選びました")
        break
    else:
        print("1~3を選んでください")
        continue