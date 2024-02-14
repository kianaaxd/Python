

def shape(length, width):
    area = length * width
    perimeter = 2 * (length + width)
    return area, perimeter

length = float(input("Enter the length of the shape: "))
width = float(input("Enter the width of the shape: "))
area ,perimeter = shape(length, width)

print("The area is", area, "and the the perimeter is", perimeter)

if length == width:
    print("The shape is Square")

else:
    print("The shape is Rectangle")