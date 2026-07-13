a = int(input("Enter your Bill Amount: "))

if a>=1000:
    print("Your Total Amount is: ",a-(a * 10/100))
else:
    print("Your total amount is: ",a)