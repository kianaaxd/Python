num1 = int(input("Enter your mark in Physics: "))
num2 = int(input("Enter your mark in Chemistry: "))
num3 = int(input("Enter your mark in Biology: "))
num4 = int(input("Enter your mark in Mathematics: "))
num5 = int(input("Enter your mark in Computer: "))

percent = (num1 + num2 + num3 + num4 + num5) / 5

print(f"Your total Average in subjects are {percent:.2f}%")

if percent >= 90:
        print("Your Grade: Grade A")

elif percent >= 80:
        print("Your Grade: Grade B")

elif percent >= 70:
        print("Your Grade: Grade C")

elif percent >= 60:
        print("Your Grade: Grade D")

elif percent >= 40:
        print("Your Grade: Grade E")

else:
        print("Your Grade: Grade F")



