class Account(object):

    count = 0

    def __init__(self, balance, name):
        self.balance = balance
        self.name = name
        self.account_number = Account.count
        Account.count += 1

    def withdraw(self, money):
        if money > self.balance:
            print("残金が足りません")
        else:
            self.balance = self.balance - money
            self.show_balance()

    def deposit(self, money):
        self.balance = self.balance + money
        self.show_balance()

    def show_balance(self):
        print(f"{self.account_number}：{self.name}の残金は{self.balance}円です")


Daisuke = Account(10000, "Daisuke")

Daisuke.withdraw(1400)
Daisuke.deposit(4500)
Daisuke.withdraw(100000)

Sasakawa = Account(10000, "Sasakawa")
Sasakawa.withdraw(4000)