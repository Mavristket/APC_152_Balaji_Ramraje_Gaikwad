import csv

file_name = "transactions.csv"
total_deposits = 0
total_withdrawals = 0
transactions = []

with open(file_name, "r", newline="") as file:
    for transaction in csv.DictReader(file):
        amount = float(transaction["Amount"])
        transactions.append((transaction["Type"], amount))
        if transaction["Type"].lower() == "deposit":
            total_deposits += amount
        elif transaction["Type"].lower() == "withdrawal":
            total_withdrawals += amount

balance = total_deposits - total_withdrawals
largest = max(transactions, key=lambda transaction: transaction[1])

print("Total deposits:", total_deposits)
print("Total withdrawals:", total_withdrawals)
print("Final balance:", balance)
print("Largest transaction:", largest[0], largest[1])
