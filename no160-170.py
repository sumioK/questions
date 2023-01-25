# 161
i = 0
while i > 3:
  print(i)
  i += 1
else:
  print('終了')

# 162
A = [1, 2, 3, 4]
for i in A:
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