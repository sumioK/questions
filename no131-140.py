# 131
d = {1: 'one', 2: 'two', 3:'three'}
for i in d.values():
  print(i)

# 132
data = ['one', 'two', 'three']
for i, d in enumerate(data):
  print(i, d)

# 133
data1 = ['1', '2', '3']
data2 = ['one', 'two', 'three']
for d1, d2 in zip(data1, data2):
  print(d1, d2)

# 134
data = [1, 3 , 5, 7]
for d in reversed(data):
  print(d)

# 135
keys = ['one', 'two', 'three']
values = [10, 20, 30]
dict = {}
for k, v in zip(keys, values):
  dict[k] = v
print(dict)
