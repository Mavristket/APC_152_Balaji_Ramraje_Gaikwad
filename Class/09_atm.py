class ATM:
    def __init__(self, account_holder, account_number, balance=0):
        self.account_holder = account_holder
        self.account_number = account_number
        self.balance = balance

    def check_balance(self):
        print("Current Balance: Rs.", round(self.balance, 2))

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print("Amount deposited successfully.")
        else:
            print("Amount must be greater than zero.")

    def withdraw(self, amount):
        if amount <= 0:
            print("Amount must be greater than zero.")
        elif amount > self.balance:
            print("Insufficient balance.")
        else:
            self.balance -= amount
            print("Please collect your cash.")

    def display_details(self):
        print("Account Holder:", self.account_holder)
        print("Account Number:", self.account_number)
        print("Balance: Rs.", round(self.balance, 2))


atm = ATM("Amit", "1234567890", 5000)

while True:
    print("\n--- ATM MENU ---")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Display Account Details")
    print("5. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        atm.check_balance()
    elif choice == "2":
        amount = float(input("Enter deposit amount: Rs. "))
        atm.deposit(amount)
    elif choice == "3":
        amount = float(input("Enter withdrawal amount: Rs. "))
        atm.withdraw(amount)
    elif choice == "4":
        atm.display_details()
    elif choice == "5":
        print("Thank you for using the ATM.")
        break
    else:
        print("Invalid choice. Please try again.")
