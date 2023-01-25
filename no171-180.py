# 171
li = [1, 2, 3, 4, 5]
for i,num in enumerate(li):
  if i %2 == 0:
    print(num)

# 172
word = "WORD"
for i , e in enumerate(word):
  print(i, e)

# 173
word = "WORD"
for i , e in enumerate(word):
  print(i, e, sep='-')

# 174
word = "WORD"
for i , e in enumerate(word):
  print(i, e, sep='-', end='-')

# 175
word = "WORD"
num = '0123'
for n , w in zip(num, word):
  print("{}-{}".format(n, w))

# 176
li = [5, 4, 3, 2, 1]
ans_li = [idx + elem for idx, elem in enumerate(li)]
print(ans_li)

# 177
li = [11, 22, 33, 44, 55]
if 44 in li:
  print(True)
else:
  print(False)

# 178
li = [1, 2, 3, 4, 5]
t = (li[0], li[-1])
print(t)