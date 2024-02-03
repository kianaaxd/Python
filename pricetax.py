price = float(input("Enter the price of the item: "))
province = int(input("Enter the province code: "))

if province == 1:
    Totalprice = price + price * 0.05
    print(f"Total price = ",Totalprice)
else: 
    Totalprice = price + price * 0.15

    print(f"Total price = ",Totalprice)


