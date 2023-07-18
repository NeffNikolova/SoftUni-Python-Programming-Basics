name_player_1 = input()
name_player_2 = input()

pts_1 = 0
pts_2 = 0
winner_name = ''
pts_winner = 0

end = False
wars = False
while True:
    card_pl_1 = input()

    if card_pl_1 == 'End of game':
        end = True
        break
    else:
        card_pl_2 = input()
        card_pl_1 = int(card_pl_1)
        card_pl_2 = int(card_pl_2)

        if card_pl_1 > card_pl_2:
            pts_1 += (card_pl_1 - card_pl_2)
        elif card_pl_1 < card_pl_2:
            pts_2 += (card_pl_2 - card_pl_1)
        elif card_pl_1 == card_pl_2:
            wars = True
            card_pl_1 = int(input())
            card_pl_2 = int(input())
            if card_pl_1 > card_pl_2:
                # pts_1 += (card_pl_1 - card_pl_2)
                winner_name = name_player_1
                pts_winner = pts_1
            elif card_pl_1 < card_pl_2:
                # pts_2 += (card_pl_2 - card_pl_1)
                winner_name = name_player_2
                pts_winner = pts_2
            break
if end:
    print(f"{name_player_1} has {pts_1} points")
    print(f"{name_player_2} has {pts_2} points")
elif wars:
    print(f"Number wars!")
    print(f"{winner_name} is winner with {pts_winner} points")






