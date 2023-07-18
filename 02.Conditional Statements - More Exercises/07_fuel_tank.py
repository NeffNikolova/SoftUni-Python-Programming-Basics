fuel = input()
fuel_in_tank = float(input())

if fuel == "Diesel" or fuel == "Gasoline" or fuel == "Gas":
    if fuel_in_tank >= 25:
        fuel = fuel.lower()
        print(f'You have enough {fuel}.')
    elif fuel_in_tank < 25:
        fuel = fuel.lower()
        print(f'Fill your tank with {fuel}!')
else:
    print('Invalid fuel!')


