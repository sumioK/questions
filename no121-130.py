# 121
d = {'x': 10, 'y': 20}
d['x'] = "AAAA"
print(d)

# 122
d = dict(x = 'AAAA', y = 20)
d['z'] = 100
print(d)

# 123
d = dict(x = 'AAAA', y = 20, z =100)
d[1] = 1000
print(d)

# 124
d = {'x': 'AAAA', 'y': 20, 'z': 100, 1: 1000}
print(d.keys())

# 125
d = {'x': 'AAAA', 'y': 20, 'z': 100, 1: 1000}
print(d.values())
