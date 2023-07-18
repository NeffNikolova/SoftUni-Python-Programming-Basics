# washing_liquid = int(input())
#
# washing_liquid *= 750
#
# stop = False
# all_plates = 0
# all_pots = 0
#
# while washing_liquid > 0:
#     for i in range(1,4):
#         if i <= 2:
#             plates_nr = input()
#             if plates_nr == 'End':
#                 stop = True
#                 break
#             else:
#                 washing_liquid -= (int(plates_nr) * 5)
#                 all_plates += int(plates_nr)
#         elif i == 3:
#             pots_nr = input()
#             if pots_nr == 'End':
#                 stop = True
#                 break
#             else:
#                 washing_liquid -= (int(pots_nr) * 15)
#                 all_pots += int(pots_nr)
#     if stop:
#         break
#
# if washing_liquid < 0:
#     print(f"Not enough detergent, {abs(washing_liquid)} ml. more necessary!")
# else:
#     print("Detergent was enough!")
#     print(f'{all_plates} dishes and {all_pots} pots were washed.')
#     print(f'Leftover detergent {washing_liquid} ml.')

washing_liquid = int(input())
washing_liquid *= 750

all_plates = 0
all_pots = 0
i = 0

while True:
    nr = input()
    i += 1
    if nr == 'End':
        break
    else:
        if i % 3 == 0:
            washing_liquid -= (int(nr) * 15)
            all_pots += int(nr)
            if washing_liquid < 0:
                break
        else:
            washing_liquid -= (int(nr) * 5)
            all_plates += int(nr)
            if washing_liquid < 0:
                break

if washing_liquid >= 0:
    print("Detergent was enough!")
    print(f'{all_plates} dishes and {all_pots} pots were washed.')
    print(f'Leftover detergent {washing_liquid} ml.')
else:
    print(f"Not enough detergent, {abs(washing_liquid)} ml. more necessary!")
