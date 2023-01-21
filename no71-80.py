# 71
world = "Hello"
print(world[2:4])

# 72
s = 'training'
print(s[1:5])

# 73
s = "understand"
n = [1, 3, 5, 7, 9]
for i in n:
  print(s[i])

print(s[1::2])

# 74
li = [1, 2, 3, 4, 5]
print(li[::-1])

# 75
mat = [[1, 2], [3, 4]]
print(mat[0][1])

# 76
c = ['red', 'blue', 'yellow']
c.append('green')
print(c)

# 77
c = ['dog', 'blue', 'yellow']
c.remove('dog')
print(c)

# 78
li1 = [1, 2, 3]
li2 = [4, 5, 6]
print(li1 + li2)

# 79
li1 = [1, 2, 3, 4, 5]
li2 = [6, 7, 8, 9, 10]
print(li1 + li2)

# 80
c = ['red', 'blue', 'yellow']
c_copy = list(c)
print(c_copy)