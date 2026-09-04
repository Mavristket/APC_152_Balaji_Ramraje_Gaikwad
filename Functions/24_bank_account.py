balance = 0
transactions = []


def deposit(amount):
    global balance
    balance += amount
    transactions.append(f"Deposited {amount}")
    return balance


def withdrawal(amount):
    global balance
    if amount > balance:
        return "Insufficient balance"
    balance -= amount
    transactions.append(f"Withdrew {amount}")
    return balance


def balance_enquiry():
    return balance


def transaction_history():
    return transactions.copy()


deposit(1000)
withdrawal(250)
print(balance_enquiry())
print(transaction_history())
