current_balance = 1000
def withdraw_money(balance, withdraw_amount):
    if withdraw_amount > balance:
        print("Transaction Failed: Balance nahi hai!")
        return balance
    else:
        new_balance = balance - withdraw_amount
        print(f"Success: ₹{withdraw_amount} nikal gaye!")
        return new_balance

print(f"Your Amount {current_balance}")
amount = int(input("Enter your amount: "))
current_balance = withdraw_money(current_balance, amount)
print(f"Your total balance: {current_balance}")