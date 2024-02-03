print("Enter a Character: ")
ch = input()

chlen = len(ch)
if chlen==1:
    asc = ord (ch)
    print("\nASCII Value of \"" +(ch)+ "\" = " +str(asc))
else:
    print("\nInvalid Input!")