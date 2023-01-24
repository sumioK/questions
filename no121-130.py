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

# 126
d = {'x': 'AAAA', 'y': 20, 'z': 100, 1: 1000}
d2 = {"x": 30, "xx": 40}
d.update(d2)
print(d)

# 127
d = {'x':30, 'y': 20, 'z': 100, 1: 1000, 'xx': 40}
print(d.get('xx'))

# 128
d = {'x':30, 'y': 20, 'z': 100, 1: 1000, 'xx': 40}
print(d.get('xxx', 'なし'))

# 129
d = {'x':30, 'y': 20, 'z': 100, 1: 1000, 'xx': 40}
d['xxx'] = d.get('xxx', '50')
print(d)

# 130
d = {'x':30, 'y': 20, 'z': 100, 1: 1000, 'xx': 40, 'xxx': '50'}
print('xxx' in d)
