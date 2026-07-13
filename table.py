a = int(input("Enter a number to print multiplication table: "))
b = int(input("Enter the range of multiplication table: "))

for i in range(1,b+1):
    print(a,"X",i,"=",a*i)
