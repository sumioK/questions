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
