# 51
n = 14
if n > 15:
  print('とても大きい数字')
elif n >= 11:
  print('中くらいの数字')
else:
  print('小さい数字')

# 52
a = 1
b = 10
if a > b:
  print(a)
else:
  print(b)

# 53
age = 20
if age >= 20:
  if age < 60:
    print('20以上60未満')

# 54
a = 5
if a %2 == 0:
  print(True)
else:
  print(False)

# 55
n = 1
if n == 1:
  print('Yes')
else:
  print('No')

# 56
s = "hello"
if s == 'hello':
  print('Yes')

# 57
s1 = 'apple'
s2 = 'lemon'
if s1 < s2:
  print('appleはlemonより前')
  # sort順で比較する

# 58
s1 = 'apple'
s2 = 'Apple'
if s1 < s2:
  print('appleはAppleより前')

# 59
s1 = 'Hello Python'
s2 = 'Python'
if s2 in s1:
  print(s2 +'は'+ s2 +'に含まれる')

# 60
if s2 not in s1:
  print(s2 +'は'+ s2 +'に含まれない')