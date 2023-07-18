tournament = input()

all_games = 0
won_games = 0
lost_games = 0

while tournament != 'End of tournaments':
    games = int(input())
    all_games += games
    for match in range(1, games + 1):
        desi_team_pts = int(input())
        other_team_pts = int(input())

        if desi_team_pts > other_team_pts:
            won_games += 1
            print(f"Game {match} of tournament {tournament}: win with {(desi_team_pts-other_team_pts)} points.")
        elif desi_team_pts < other_team_pts:
            lost_games += 1
            print(f"Game {match} of tournament {tournament}: lost with {(other_team_pts - desi_team_pts)} points.")
    tournament = input()

print(f'{(won_games/all_games*100):.2f}% matches win')
print(f'{(lost_games/all_games*100):.2f}% matches lost')



