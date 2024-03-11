def find_max(a,b,c):
    if a>b:
        return a
    elif a>c:
        return a
    elif b>c:
        return b
    else:
        return c

def main():
    a = int(input("Input the first number: "))
    b = int(input("Input the second number: "))
    c = int(input("Input the third number: "))
    x = find_max(a,b,c)
    print("The largest number is", x)


main()
