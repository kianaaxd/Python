# Get three numbers from the user
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))
num4 = float(input("Enter the fourth number: "))
num5 = float(input("Enter the fifth number: "))

# Calculate the average of the five numbers
average = (num1 + num2 + num3 + num4 + num5) / 5

#Print the average
print(f"The average of {num1}, {num2}, {num3}, {num4}, {num5} is {average}")

#Print the average with 3 decimal points
print(f"The average of {num1}, {num2}, {num3}, {num4}, {num5} is {average: .3f}")
