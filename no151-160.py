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
  
# 162
i = 0
while i < 3:
  print(i)
  i = i + 1
else:
  print('終了')

# 163
n = 1
for i in range(4):
  print(n)

# 164
i = 0
while i < 10:
  print(i)
  i += 1

# 165
for i in range(5, 10):
  print(i)

# 166
for i in range(0, 9):
  if i %2 == 0:
    continue
  print(i)
  if i == 7:
    break

# 167
for i in range(3):
  print(i)
  if i == 2:
    break
else:
  print('終了')

# 168
li = [1, 2, 3, 4, 5]
for i in li:
  if i %2 != 0:
    continue
  print(i)

# 169
li = list(range(100))
print(li)

# 170
word = ['A', 'B', 'C', 'D']
for i, w in enumerate(word):
  print('index:' + str(i),w)