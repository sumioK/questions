# 81
li = [1, 2, 3, 4, 5]
li.append(6)
li.append(7)
print(li)

# 82
li = [1, 2, 3, 4, 5]
li.append(6)
print(li)

# 83
li = [1, 2, 3, 4, 5]
li[1:4] = [10, 11, 12]

print(li)

# 84
li = [1, 2, 3, 4, 5]
del li[1]
print(li)

# 85
li = [3, 2, 1, 5, 4]
li.pop()
print(li)

# 86
li = [1, 2, 3, 4, 5]
del li[1:4]
print(li)

# 87
li = [1, 2, 3, 4, 5]
li.insert(1,100)
print(li)

# 88
li = ['orange', 'apple', 'banana', 'pieapple', 'lemon', 'apple', 'banana']
print(li.count('apple'))

# 89
li = ['orange', 'apple', 'banana', 'pineapple,', 'lemon', 'apple', 'bnana']
print(li.index('lemon'))

# 90
li = ['orange', 'apple', 'banana', 'pineapple,', 'lemon', 'apple', 'bnana']
li.reverse()
print(li)
