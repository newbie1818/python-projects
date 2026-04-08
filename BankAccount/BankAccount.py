# Class BankAccount with attributes:
# -  owner, balance
# - instance methods:
#   - deposit(amount)
#   - withdraw(amount)
#   - get_balance()

class BankAccount():

    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance = self.balance + amount
        return (f"You added up {amount}. You current balance is: {self.balance}.")

    def withdraw(self, amount):
        self.balance = self.balance - amount
        return (f"You added up {amount}. You current balance is: {self.balance}.")

    def get_balance(self):
        return (f"You balance equals: {self.balance}")


account = BankAccount("Anna", 3000)

print(account.owner)
print(account.balance)
print(account.deposit(1000))
print(account.withdraw(30))
print(account.get_balance())




