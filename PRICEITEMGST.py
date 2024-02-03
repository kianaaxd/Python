# Get price and Tax percentage from the user
price = float(input("Enter the price of item: "))
GST = float(input("Enter the GST percentage: "))

amount = price + price * (GST/100)

# Print the amount to be paid
print(f"The price of item without GST {price} with GST of {GST} is {amount: .2f}")
print(f"The price of item with GST {GST}% is {amount: .2f}")