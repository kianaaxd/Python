print ("Enter a Character: ")
c = input()
if len(c)>1:
    print("\nInvalid Input!")
else:
    if c>="a" and c<="z":
        print("\n\"" +c+ "\" It is an alphabet.")
    elif c>="A" and c<="z":
        print("\n\"" +c+ "\" It is an alphabet")
    else:
        print("\n\"" +c+ "\" It is not an alphabet!")