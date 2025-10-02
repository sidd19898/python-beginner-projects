#ask user the amount
#ask for source currency(usd/eur/cad)
#ask for target currency(usd/eur/cad)
#print ______ source currency equals to ______target currency 
"""
1) usd to cad
   1.39

2) cad to usd
   0.72

3) eur to cad
   1.64

4) cad to eur
   0.61

5) eur to usd 
   1.17

6) usd to eur
   0.85
"""
a = float(input("Enter the amount : "))
b = input("source currency(usd/eur/cad):")
c = input("target currency(usd/eur/cad):")
if(b == "usd" and c == "cad"):
    d = a * 1.39
    print(a,"equals to",d)
elif(b == "cad" and c == "usd"):
    d = a * 0.72
    print(a,"equals to",d)
elif(b == "eur" and c == "cad"):
    d = a * 1.64
    print(a,"equals to",d)
elif(b == "cad" and c == "eur"):
    d = a * 0.61
    print(a,"equals to",d)
elif(b == "eur" and c == "usd"):
    d = a * 1.17
    print(a,"equals to",d)
elif(b == "usd" and c == "eur"):
    d = a * 0.85
    print(a,"equals to",d)