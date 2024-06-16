class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.__balance = balance  # Private attribute

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited {amount}, new balance is {self.__balance}")
        else:
            print("Deposit amount must be positive")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrew {amount}, new balance is {self.__balance}")
        else:
            print("Invalid withdraw amount")

    def get_balance(self):
        return self.__balance

# Create an instance of BankAccount
account = BankAccount("Alice", 1000)

# Accessing public methods
account.deposit(500)
account.withdraw(200)

# Trying to access the private attribute directly (will fail)
# print(account.__balance)  # AttributeError

# Accessing the private attribute using a public method
print("Final balance:", account.get_balance())
