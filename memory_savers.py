import copy

print('Memmory savers')
print('-'*80)

my_lambda = lambda x, y: x + y

my_sum = my_lambda(2, 3)

print(my_sum)

players = [
    {
        'first_name': 'John',
        'last_name': 'Doe',
        'rank': 3
    },
    {
        'first_name': 'Kevin',
        'last_name': 'McDonald',
        'rank': 1
    },
    {
        'first_name': 'Brad',
        'last_name': 'Kelvin',
        'rank': 2
    }
]

print(players)

sorted_players = sorted(players, key = lambda player: player['rank'])
print(sorted_players)

def check_top_3_players(player):
    updated_player = copy.deepcopy(player)
    updated_player['is_top_3'] = True if player['rank'] <= 3 else False
    return updated_player

top_players = list(map(check_top_3_players, players))

print(top_players)

all_mcdonalds = list(filter(lambda player: player['last_name'] == 'McDonald', players))
print(all_mcdonalds)

# zip
letters = ['a', 'b', 'c', 'z']
numbers = [1, 2, 3]

print(zip(letters, numbers))

for l, nr in zip(letters, numbers):
    print(nr, l)

#list comprehension

my_numbers = list(range(1,6))
print(my_numbers)
even_sqared_numbers = [item ** 2 for item in my_numbers if item % 2 == 0]
print(even_sqared_numbers)
