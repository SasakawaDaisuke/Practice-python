# input():ユーザーが入力した値を取得する

age_casino = 18
age = int(input("何歳ですか:"))
game_text = """
1:ルーレット
2:ブラックジャック
3:ポーカー
"""

if age >= age_casino:
    print("カジノにようこそ")
    game = input(game_text)
    if game == "1":
        print("あなたはルーレットを選びました")
    elif game == "2":
        print("あなたはブラックジャックを選びました")
    elif game == "3":
        print("あなたはポーカーを選びました")
    else:
        print("1~3を選んでください")
else:
    print("18歳未満は入場できません")