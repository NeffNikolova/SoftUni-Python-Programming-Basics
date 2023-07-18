room_rent = int(input())

statuettes_price = room_rent * 0.70
catering_price = statuettes_price * 0.85
sound_price = catering_price * 0.50

total_expenses = room_rent + statuettes_price + catering_price + sound_price

print(f'{total_expenses:.2f}')
