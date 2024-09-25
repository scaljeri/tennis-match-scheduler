import os
import argparse
import random
import pandas as pd

def add_players_to_games(games = [], gender = 'M/F', max_per_game = 4 ):
  for idx, d in enumerate(dates):
    random.shuffle(players)
    sorted_players = sorted(players, key=lambda player: played[player])
    if idx < len(games):
      game = games[idx]
    else:
      game = []
      games.append(game)
    for p in sorted_players:
      if len(game) == max_per_game:
        break
      elif (
        d not in blocker[p] and 
        played[p] < max_games[p] and 
        (gender == 'M/F' or genders[p] == gender) and
        no_pair[p] not in game
      ):
        game.append(p)
        played[p] += 1
  return games

# Step 1: Setup argparse to handle command-line arguments
parser = argparse.ArgumentParser(description='Process CSV file with optional directory.')
parser.add_argument('--dir', type=str, default='.', help='Directory where the CSV file is located (default: current directory).')
parser.add_argument('--mix-only', action='store_true', default=False, help='Is this competition Mix only (default: False).')

# Step 2: Parse the arguments
args = parser.parse_args()

df_setup = pd.read_csv(os.path.join(args.dir, './players.csv'))
df_dates = pd.read_csv(os.path.join(args.dir, './tennis_match_schedule.csv'))

played = {}
dates = df_dates['Date'].to_list()
players = []
blocker = {}
max_games = {}
genders = {}
no_pair = {}

for index, row in df_setup.iterrows():
    name = row['name']
    players.append(name)
    blocker[name] = row['blocker'].strip().split() if pd.notna(row['blocker']) else []
    max_games[name] = row['max_games']
    played[name] = 0
    genders[name] = row['gender']
    no_pair[name] = row['no_pair_with']

for idx, p in enumerate(players):
    print(f"{p.ljust(10)} {idx}: {', '.join(blocker[p])}")

print('---------') 

if args.mix_only:
  games = add_players_to_games([], 'M', 2)
  games = add_players_to_games(games, 'F', 4)
else:
  games = add_players_to_games()

for idx, g in enumerate(games):
  game_players = list(map(lambda name: f"{name}({genders[name]})", g))
  # print(game_players)
  # print(f"len={len(dates)} idx={idx}")

  print(f"{dates[idx]}: {', '.join(game_players)}")

for p in players:
  print(f"{p.ljust(10)} ({played[p]})")