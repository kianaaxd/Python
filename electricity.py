unit = float(input("Input your unit: "))


if unit <= 50:
    price = unit * 0.50
    surcharge = (unit * 0.50) * .2
    bill = price + surcharge
    print("Total bill is $%.2f" % bill)

elif 50< unit <= 150:
    excess = (unit - 50) * .75
    pricelimit = 50 * 0.5
    overall = pricelimit + excess
    a1 = overall * 0.2
    bill2 = a1 + overall
    print("Total bill is $%.2f" % bill2)

elif unit <= 250:
    excess1 = (unit - 150) * 1.2
    pricelimit1 = 50 * 0.5
    pricelimit2 = 100 * .75
    overall = pricelimit1 + pricelimit2 + excess1
    a2 = overall * 0.2
    bill3 = a2 +overall
    print("Total bill is $%.2f" %  bill3) 

elif unit > 250:
    excess2 = (unit - 250) * 1.5
    pricelimit3 = 50 * 0.5
    pricelimit4 = 100 * 0.75
    pricelimit5 = 100 * 1.2
    overall = pricelimit3 + pricelimit4 +pricelimit5 + excess2
    a3 = overall * 0.2
    bill4 = a3 + overall
    print("Total bill is $%.2f" % bill4)

