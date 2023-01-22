# 101
town = {'Aichi': 'Nagoya', 'Kanagawa': 'Yokohama'}
print('Aichiは' + town['Aichi'] + 'です')
print('Kanagawaは' + town['Kanagawa'] + 'です')

# 102
town['Hokkaido'] = 'Hakodate'
print(town)

# 103
town['Hokkaido'] = 'Sapporo'
print(town)

# 104
del town['Aichi']
print(town)

# 105
keys =list(town.keys())
print(keys)

# 106
print(list(town.values()))

# 107
print(list(town.items()))

# 108
print(town.get('Okinanwa'))

# 109
print(town.get("Okinawa", 'なし'))

# 110
# if not town.get('Okinawa'):
#   town['Okinawa'] = 'Naha'
# print(town)
town['Okinawa'] = town.get('Okinawa', 'Naha')
print(town)
