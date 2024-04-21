def convert_base(number, from_base, to_base):
    if from_base < 2 or from_base > 16 or to_base < 2 or to_base > 16:
        return "Base out of range. Please choose a base between 2 and 16."

    # Define a dictionary to map digits to their values in bases greater than 10
    digits_map = {10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}

    # Define a reverse dictionary for the conversion
    reverse_map = {v: k for k, v in digits_map.items()}

    # Convert the number to base 10 first
    base_10_number = 0
    power = len(number) - 1
    for digit in number:
        if digit.isdigit():
            base_10_number += int(digit) * (from_base ** power)
        
        else:
            base_10_number += int(digit) * (from_base ** power)
            power -= 1

    # Convert the base 10 number to the desired base
    converted_number = ""
    while base_10_number > 0:
        remainder = base_10_number % to_base
        if remainder >= 10:
            converted_number = digits_map[remainder] + converted_number
        else:
            converted_number = str(remainder) + converted_number
        base_10_number //= to_base

    return converted_number


#Input from the user
number = input("Enter the number you want to convert: ")
from_base = int(input("Enter the base of the number: "))
to_base = int(input("Enter the base to convert to: "))

#Convert and display the result
result = convert_base(number, from_base, to_base)
print(f"The converted number is: {result}")