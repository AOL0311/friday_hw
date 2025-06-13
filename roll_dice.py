import random
from collections import Counter, defaultdict

def player_count():
    while True:
        try:
            players = int(input('請輸入本次遊戲人數 (2 人以上):'))
            if players <= 1:
                print('請輸入人數至少達 2 人!')
                continue
            return players
        except ValueError:
            print('請輸入有效的數字!')

def player_turn(name, max_roll=3):
    print('-' * (len(name) + 14))
    print(f'輪到玩家 {name} 投擲')
    print('-' * (len(name) + 14))
    roll = 0
    final_hand = None
    
    while roll < max_roll:
        if not auto_roll:
            input(f'按 "Enter" 鑑進行第 {roll + 1} 次投擲')
        else:
            print(f'自動進行第 {roll + 1} 次投擲')
        dice = roll_dice()
        roll += 1
        print_dice(dice)
        hand = analyze_dice(dice)
        print(f'結果: {hand[2]}')
        
        if hand[0] != '沒點':
            final_hand = hand
            break
        else:
            if roll < max_roll:
                print(f'目前沒點，還可以重骰 {max_roll - roll} 次。')
        print()
        
        if final_hand is None:
            final_hand = ('沒點', 0, '沒點')
    
    return final_hand

def roll_dice(dice_num=4):
    return [random.randint(1, 6) for _ in range(dice_num)]

def print_dice(dice):
    dice_str = ' '.join(str(x) for x in dice)
    print(f'\n投擲結果: {dice_str}')

def analyze_dice(dice):
    counts = Counter(dice)
    count_values = sorted(counts.values(), reverse=True)
    dice_sorted = sorted(dice, reverse=True)
    
    if count_values == [4]:
        point = dice[0]
        detail = f'豹子({point})'
        return ('豹子', point, detail)
    elif count_values == [3, 1]:
        point = dice_sorted[0]
        detail = f'沒點 {point}大'
        return ('沒點', point, detail)
    elif count_values == [2, 2]:
        point = sum([x for x, y in counts.items() if y == 2])
        detail = f'{point}點'
        return ('有點', point, detail)
    elif count_values == [2, 1, 1]:
        point = sum([x for x, y in counts.items() if y == 1])
        detail = f'{point}點'
        return ('有點', point, detail)
    else:
        point = dice_sorted[0]
        detail = f'沒點 {point}大'
        return ('沒點', point, detail)

def rank(result):
    type, point, _ = result
    order = {1: 6, 6: 5, 5: 4, 4: 3, 3: 2, 2: 1}
    
    if type == '豹子':
        type_rank = 3
        main_rank = order.get(point, 0)
    elif type == '有點':
        type_rank = 2
        main_rank = point
    else:
        type_rank = 1
        main_rank = point
        
    return (type_rank, main_rank)

def break_ties(players):
    tie_result = []
    for player in players:
        final_hand = player_turn(player['name'])
        player['final_hand'] = final_hand
        player['rank'] = rank(final_hand)
        tie_result.append(player)
        
    sorted_tie_result = sorted(tie_result, key=lambda x: x['rank'], reverse=True)
    
    ranks = defaultdict(list)
    for player in sorted_tie_result:
        ranks[player['rank']].append(player)
    
    final_order = []
    for rank_key in sorted(ranks.keys(), reverse=True):
        player_group = ranks[rank_key]
        
        if len(player_group) == 1:
            final_order.append(player_group[0])
        else:
            print(f'\n{len(player_group)} 名玩家再次平手，繼續加賽!')
            final_order.extend(break_ties(player_group))
            
    return final_order

players_count = player_count()

players = []
for i in range(players_count):
    while True:
        name = str(input(f'請輸入玩家{i + 1}名稱:')).strip()
        if not name:
            print('請輸入玩家名稱!')
        elif name in [x['name'] for x in players]:
            print('玩家名稱重複!')
        else:
            break
    players.append({'name': name})
    
auto_roll_input = str(input('是否要省略擲骰子的過程(y/n)?').strip().lower())
auto_roll = (auto_roll_input == 'y')

print('\n開始遊戲!\n')

for player in players:
    final_hand = player_turn(player['name'])
    player['final_hand'] = final_hand
    player['rank'] = rank(final_hand)
    print()

# print('當前排名如下:')
sorted_players = sorted(players, key=lambda x: x['rank'], reverse=True)
max_name_len = max(len(x['name']) for x in sorted_players)

# print(f'{"排名":<5} {"玩家名稱":<{max_name_len}} 結果說明')
# for i, player in enumerate(sorted_players, start=1):
#     name = player['name']
#     detail = player['final_hand'][2]
#     print(f'{i:<5} {name:<{max_name_len}} {detail}')
# print()

ranks = defaultdict(list)
for player in sorted_players:
    ranks[player['rank']].append(player)

final_rank = []
current_rank = 1

for rank_key in sorted(ranks.keys(), reverse=True):
    same_rank = ranks[rank_key]
    if len(same_rank) == 1:
        player = same_rank[0]
        player['final_rank'] = current_rank
        final_rank.append(player)
        current_rank += 1
    else:
        print(f'名次 {current_rank} ~ {current_rank + len(same_rank) - 1} 名平手，進行加賽!')
        tie_order = break_ties(same_rank)
        
        for player in tie_order:
            player['final_rank'] = current_rank
            final_rank.append(player)
            current_rank += 1

print('最終排名結果如下:')
sorted_final_rank = sorted(final_rank, key=lambda x: x['final_rank'])
print(f'{"排名":<5}\t{"玩家名稱":<{max_name_len}}\t結果說明')
for player in sorted_final_rank:
    print(f'{player["final_rank"]:<5}\t{player["name"]:<{max_name_len}}\t{player["final_hand"][2]}')

print('\n遊戲結束\n')