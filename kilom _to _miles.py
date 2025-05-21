# Taking  kilomiters input from the user
kilometers = float(input("Enter value in kilometers: "))

# convertion factory
conv_fac = 0.621371

# calculate miles
miles = kilometers * conv_fac
print("%0.2f kilometers in equal to %0.2f miles"%(kilometers,miles))