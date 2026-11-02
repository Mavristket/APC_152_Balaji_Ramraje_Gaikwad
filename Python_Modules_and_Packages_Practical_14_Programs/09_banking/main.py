from banking.account import *
from banking.transaction import *
from banking.loan import loan_amount
name=input("Account holder: "); balance=float(input("Opening balance: "))
a=create_account(name,balance)
print("After deposit =",deposit(a,1000)); print("After withdrawal =",withdrawal(a,500))
print("Balance =",get_balance(a))
p=float(input("Loan amount: ")); r=float(input("Rate: ")); t=float(input("Years: "))
print("Loan total =",loan_amount(p,r,t))
