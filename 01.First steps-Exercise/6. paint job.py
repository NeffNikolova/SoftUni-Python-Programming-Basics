nylonprice=1.50
paintprice=14.50
thinnerprice=5

needednylon=int(input())
neededpaint=int(input())
neededthinner=int(input())
workinghrs=int(input())

nylon=((needednylon+2)*nylonprice)
paint=((neededpaint*1.10)*paintprice)
thinner=(neededthinner*thinnerprice)
bags=0.40

workprice=(nylon+paint+thinner+bags)*0.30

expences=nylon+paint+thinner+bags+(workprice*workinghrs)

print(expences)