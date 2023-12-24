from datetime import datetime


class Client:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.accounts = []

    def create_account(self, account_type, initial_balance=0):
        if account_type == "Сберегательный счёт":
            account = SavingsAccount(initial_balance)
        elif account_type == "Кредитный счёт":
            account = CreditAccount(initial_balance)
        else:
            raise ValueError("Нет такого типа счёта")
        self.accounts.append(account)
        return account


class Account:
    def __init__(self, balance=0):
        self.balance = balance
        self.transactions = []

    def accrual(self, amount):
        if amount > 0:
            self.balance += amount
            self._add_transaction(amount, "Начислить")

    def deduction(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            self._add_transaction(amount, "Вычет")
        else:
            raise ValueError("На белансе недостаточно средств")

    def get_balance(self):
        return self.balance

    def _add_transaction(self, amount, transaction_type):
        transaction = {
            "сумма": amount,
            "дата": datetime.now(),
            "тип": transaction_type
        }
        self.transactions.append(transaction)


class SavingsAccount(Account):
    def __init__(self, balance=0, interest_rate=0.02):
        super().__init__(balance)
        self.interest_rate = interest_rate

    def calculate_interest(self):
        interest = self.balance * self.interest_rate
        self.accrual(interest)
        return interest


class CreditAccount(Account):
    def __init__(self, balance=0, credit_limit=1000, interest_rate=0.05):
        super().__init__(balance)
        self.credit_limit = credit_limit
        self.interest_rate = interest_rate

    def deduction(self, amount):
        if amount > self.balance + self.credit_limit:
            raise ValueError("Invalid withdrawal amount")
        super().deduction(amount)

    def calculate_interest(self):
        interest = self.balance * self.interest_rate
        self.accrual(interest)
        return interest


# Пример использования:

c = Client("John Doe", "123 Main St")

saving = c.create_account("Сберегательный счёт", 5000)
credit = c.create_account("Кредитный счёт", 2000)

saving.deduction(1000)
credit.accrual(1500)

print("Сберегательный счёт:", saving.get_balance())
print("Кредитный счёт:", credit.get_balance())
