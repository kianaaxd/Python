number = int(input("Enter a number: "))
for x in range(1, number + 1):
    if x == 4:
        continue 
    print ("Current Number is:", x, "and the cube is", x**3)
