

print("1. Addition \n2. Subtraction \n3. Multiplication \n4. Division \n5. Exit")
num1 = int(input("Enter your choice (1-5): "))

if  num1 == 5:

    print("Have a great day!")

elif not (num1 <= 4 and  num1 >= 1):
    print("invalid")

else:
    
    num2 = int(input("Enter Two Number: "))
    num3 = int(input())
    
    if num1 == 1:
        sum = num2 + num3
        print(f"The sum of the numbers is = ", sum)
    elif num1 == 2:
        difference = num2 - num3
        print(f"The difference of the numbers is = ", difference)

    elif num1 == 3:
        product = num2 * num3
        print(f"The product of the numbers is = ", product)

    elif num1 == 4:
        quotient = num2 / num3
        print(f"The quotient of the numbers is = ", quotient)

    


