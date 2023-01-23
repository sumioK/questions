# 111
town = {'Kanagawa': 'Yokohama', 'Hokkaido': 'Sapporo', 'Okinawa': 'Naha'}
for s in town:
  print(s)

# 112
town = {'Kanagawa': 'Yokohama', 'Hokkaido': 'Sapporo', 'Okinawa': 'Naha'}
for k, v in town.items():
  print(f'{k}は{v}です')

# 114 **
town = {'Kanagawa': 'Yokohama', 'Hokkaido': 'Sapporo', 'Okinawa': 'Naha'}
print('Kanagawa' in town)

# 115 ***
town = {'Kanagawa': 'Yokohama', 'Hokkaido': 'Sapporo', 'Okinawa': 'Naha'}
print('Kanagawa' in town.values())

# 116
d = {'x': 10, 'y': 20}
print(d)

# 117
d = dict(x = 10, y = 20)
print(d)

# 118
d = {'x': 10, 'y': 20}
print(type(d))

# 119
d = {'x': 10, 'y': 20}
print(d['x'])

# 120
d = {'x': 10, 'y': 20}
d['x'] = 100
print(d)

