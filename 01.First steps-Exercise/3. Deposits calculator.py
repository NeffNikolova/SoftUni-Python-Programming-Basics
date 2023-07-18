depositsum=float(input())
deposittime=int(input())
interest=float(input())

sum=depositsum + deposittime*((depositsum*(interest/100))/12)

print(str(sum))

