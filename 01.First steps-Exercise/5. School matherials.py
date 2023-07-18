pencilprice=5.8
markerprice=7.2
cleanerprice=1.2

pencilnr=int(input())
markernr=int(input())
cleanerlrs=int(input())

discount=int(input())/100

money=round(((pencilnr*pencilprice)+(markernr*markerprice)+(cleanerlrs*cleanerprice))*(1-discount),2)

print(money)