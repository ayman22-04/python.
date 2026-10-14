bank_balance = 5000

def deposit(amount):
    global bank_balance

    if amount > 0:
        bank_balance += amount
        print("Deposit Successful:", amount)
    else:
        print("Invalid deposit amount.")

def withdraw(amount):
    global bank_balance

    if amount <= 0:
        print("Invalid withdrawal amount.")
    elif amount <= bank_balance:
        bank_balance -= amount
        print("Withdrawal Successful:", amount)
    else:
        print("Insufficient Balance.")

print("Initial Balance:", bank_balance)

deposit(1000)
print("Updated Balance:", bank_balance)

withdraw(2000)
print("Updated Balance:", bank_balance)

withdraw(5000)
print("Final Balance:", bank_balance)