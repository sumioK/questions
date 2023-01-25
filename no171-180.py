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