# 151
a = [2, 4, 6, 8]
for i in a:
  print(i)

# 152
a = (2, 4, 6, 8)
for i in a:
  print(i)

# 153
a = {2, 3, 6, 8}
for i in a:
  print(i)

# 154
d = {1: 'one', 2: 'two', 3: 'three'}
for k, v in d.items():
  print(k, v)

# 156
x = 5
while x > 0:
  print(x - 1)
  x -= 1

# 157
x = 0
while x <= 4:
  print(x)
  x += 1

# 158
i = 0
while i < 4:
  print(i)
  if i == 2:
    break
  i += 1

# 159
i = 0
while i < 4:
  i = i + 1
  if i == 2:
    continue
  print(i)
  
