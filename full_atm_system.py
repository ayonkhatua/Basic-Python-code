current_balance = 1000

def withdraw_money(balance, withdraw_amount):
    # 🔴 1. Condition sahi ki (amount bada hai balance se)
    if withdraw_amount > balance:
        print("❌ Transaction Failed: Balance nahi hai!")
        return balance
    else:
        new_balance = balance - withdraw_amount
        # 🔴 2. Print mein withdraw_amount dikhaya
        print(f"✅ Success: ₹{withdraw_amount} nikal gaye!")
        return new_balance

def deposit_money(balance, deposit_amount):
    new_balance = balance + deposit_amount
    print(f"✅ Success: ₹{deposit_amount} jama ho gaye!")
    return new_balance

user_choice = ""

while user_choice != 4:
    print("\n--- ATM MENU ---")
    print("1. Check Balance")
    print("2. Withdraw Money")
    print("3. Deposit Money")
    print("4. Exit")
    
    user_choice = int(input("Enter your choice (1-4): "))
    
    if user_choice == 1:
        print(f"Your balance is: ₹{current_balance}")
        
    elif user_choice == 2:
        amount = int(input("Enter amount to withdraw: "))
        # 🔴 3. Asli variables bheje aur return value ko save kiya
        current_balance = withdraw_money(current_balance, amount)
        
    elif user_choice == 3:
        amount = int(input("Enter amount to deposit: "))
        # 🔴 4. Same yahan bhi asli variables bheje aur save kiya
        current_balance = deposit_money(current_balance, amount)
        
    elif user_choice == 4:
        print("Thank You for using our ATM!")
    else:
        print("Invalid Choice! Please select between 1-4.")