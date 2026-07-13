a = int(input("Enter your Bengali marks: "))
b = int(input("Enter your English marks: "))
c = int(input("Enter your Mathematics marks: "))

total_marks = a + b + c
avarage_marks = total_marks / 3
print("Your average marks is: ",avarage_marks)

if avarage_marks >= 75:
    print("Grade: A (Excellent)")
elif avarage_marks >= 60:
    print("Grade: B (Good)")
elif avarage_marks >= 35:
    print("Grade: C (Satisfactory)")
else:
    print("Grade: F (Fail)")