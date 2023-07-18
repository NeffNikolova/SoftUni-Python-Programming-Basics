lenght=int(input())
width=int(input())
height=int(input())
percent=float(input())
percentuse=percent/100

watervolumeincm=(lenght*width*height)*(1-percentuse)
watervolume=watervolumeincm/1000
print(watervolume)
