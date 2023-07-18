chickenmenuprice=10.35
fishmenuprice=12.40
vegiemenuprice=8.15

deliveryprice=2.50

chickenmenunr=int(input())
fishmenunr=int(input())
vegiemenunr=int(input())

pricefood=round((chickenmenuprice*chickenmenunr)+(fishmenuprice*fishmenunr)+(vegiemenuprice*vegiemenunr),2)
desert=round((pricefood*0.20),2)

Orderprice=round((pricefood+desert+deliveryprice),2)
print(Orderprice)