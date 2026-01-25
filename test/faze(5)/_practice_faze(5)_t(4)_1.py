# Мини задание 1
class Counter:
    def __init__(self, start=0):
        self.count = start

    def increment(self):
        self.count += 1

    def get_value(self):
        return self.count


c1 = Counter()
c2 = Counter(10)

c1.increment()
c2.increment()

print(c1.get_value())
print(c2.get_value())



class BankAccount:
    def __init__(self, balance):
        if balance < 0:
            raise ValueError("Initial balance cannot be negative")
        self._balance = balance

    @property
    def balance(self):
        return self._balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive")
        self._balance += amount

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive")
        if amount > self._balance:
            raise ValueError("Insufficient funds")
        self._balance -= amount


account = BankAccount(100)

try:
    account.deposit(-20)
except ValueError as e:
    print(f"Error: {e}")

try:
    account.withdraw(20)
except ValueError as e:
    print(f"Error: {e}")

print(account.balance)



