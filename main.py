class BankAccount:
    bank_name = "MyBank"  # Class attribute

    def __init__(self, account_number, balance):
        self._account_number = account_number  # Protected attribute
        self.__balance = balance  # Private attribute

    @property
    def account_number(self):
        return self._account_number

    @property
    def balance(self):
        return self.__balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited {amount}. New balance: {self.__balance}")
        else:
            print("Deposit amount must be greater than 0.")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrew {amount}. New balance: {self.__balance}")
        else:
            print("Withdrawal amount exceeds balance.")

    @classmethod
    def change_bank_name(cls, new_name):
        cls.bank_name = new_name
        print(f"Bank name changed to: {cls.bank_name}")

    @staticmethod
    def is_valid_account_number(account_number):
        return len(str(account_number)) == 10

    def __str__(self):
        return f"Account Number: {self._account_number}, Balance: {self.__balance}"

    def __repr__(self):
        return f"BankAccount(account_number={self._account_number}, balance={self.__balance})"


# Usage
account1 = BankAccount("1234567890", 1000)
print(account1)  # Output: Account Number: 1234567890, Balance: 1000

account1.deposit(500)  # Deposited 500. New balance: 1500
account1.withdraw(200)  # Withdrew 200. New balance: 1300

print(account1.balance)  # Output: 1300
print(account1.account_number)  # Output: 1234567890

# Trying to access private attributes directly will result in an error
# print(account1.__balance)  # This will raise an AttributeError

# Changing bank name using class method
BankAccount.change_bank_name("NewBank")
print(BankAccount.bank_name)  # Output: NewBank

# Checking account number validity using static method
print(BankAccount.is_valid_account_number(1234567890))  # Output: True




