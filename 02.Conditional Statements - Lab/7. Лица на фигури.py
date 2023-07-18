figure = str(input())
area = 0

if figure == 'square':
    sidelength = float(input())
    area = (round((sidelength*sidelength),3))
elif figure == 'rectangle':
        sideA = float(input())
        sideB = float(input())
        area = round((sideA*sideB),3)
elif figure == 'circle':
            radius = float(input())
            from math import pi
            area = round((pi*radius*radius),3)
elif figure == 'triangle':
                sideA = float(input())
                heightA = float(input())
                area = round((sideA*heightA/2),3)
print( f'{area:.3f}')
