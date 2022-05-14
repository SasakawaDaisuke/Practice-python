# 静的型付け言語(Pythonのスタイルではない)
def add_nums(a: int, b: int) -> int:
    return a + b

# 動的型付け言語
print(add_nums(1, 3))
print(add_nums("1", "3"))  # 強制するものではない
