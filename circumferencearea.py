pi = 3.14

def area(radius):
    return (pi * radius ** 2)

def circumference(radius):
    return (2 * pi * radius)


def circledetails():
    x = float(input("Enter radius: "))
    circ_a = area(x)
    circ_c = circumference(x)
    print(circ_a)
    print(circ_c)

circledetails()






