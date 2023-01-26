# 181
r = [x for x in range(10)]
print(r)

# 182
print([i*5 for i in range(1, 10)])

# 183
print([i*2 for i in range(5)])
print([i for i in range(10) if i %2 == 0])

# 184
A = [1, 2, 3, 4, 5, 6, 7, 8, 9]
x =[i*10 for i in A]
print(x)

# 185
x = [1, 2, 3]
y = [1, 2, 3]
a = [[x, y] for x in [1, 2, 3] for y in [1, 2, 3]]
print(a)

# 186
x = [1, 2, 3]
y = [1, 2, 3]
a = [[x, y] for x in [1, 2, 3] for y in [1, 2, 3] if x !=  y]
print(a)

# 187
x = ['グー', 'チョキ', 'パー']
y = ['グー', 'チョキ', 'パー']