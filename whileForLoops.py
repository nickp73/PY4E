# Indefinite loops
# While loop
"""
n = 10
while n > 0:
    print(n)
    n -= 1
print('Blastoff!')
print(n)

while True:
    line = input('> ')
    if line == 'done':
        break
    print(line)
print('Done!')

# Continue loop
while True:
    line = input('> ')
    if line[0] == '#':
        continue
    if line == 'done':
        break
    print(line)
print('Done!')

# Definite loops
# For loops

for i in [5, 4, 3, 2, 1]:
    print(i)
print('Blastoff!')

friends = ['Joseph', 'Glenn', 'Sally']
for friend in friends:
    print('Happy New Year:', friend)
print('Done!')


largest_so_far = -1
print('Before', largest_so_far)
for the_num in [9, 41, 12, 3, 74, 15]:
    if the_num > largest_so_far:
        largest_so_far = the_num
    print(largest_so_far, the_num)
print('After', largest_so_far)"""

# Counting and summing loops
count = 0
print('Before', count,)
for value in [9, 41, 12, 3, 74, 15]:
    count += 1
    print(count, value)
print('After', count)

# Summing loops
total = 0
print('Before', total)
for value in [9, 41, 12, 3, 74, 15]:
    total += value
    print(total, value)
print('After', total)

# Average loops
count = 0
sum = 0
print('Before', count, sum)
for value in [9, 41, 12, 3, 74, 15]:
    count += 1
    sum += value
    print(count, sum, value)
print('After', count, sum, sum / count)

# Filtering in a loop

print('Before')
for value in [9, 41, 12, 3, 74, 15]:
    if value > 20:
        print('Large number', value)
print('After')

# Search using a boolean variable
found = False
print('Before', found)
for value in [9, 41, 12, 3, 74, 15]:
    if value == 3:
        found = True
        break
    print(found, value)
print('After', found)

# Finding the smallest value using None

smallest = None
print('Before', smallest)
for value in [9, 41, 12, 3, 74, 15]:
    if smallest is None or value < smallest:
        smallest = value
    print(smallest, value)
print('After', smallest)

