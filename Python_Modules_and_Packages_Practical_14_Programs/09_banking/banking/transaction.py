def deposit(a,amount): a["balance"]+=amount; return a["balance"]
def withdrawal(a,amount):
    if amount>a["balance"]: return "Insufficient balance"
    a["balance"]-=amount; return a["balance"]
