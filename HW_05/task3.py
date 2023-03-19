# v.1 1'st version. For ... in ...
for i in range(1, 6):
    j1 = ''
    for j in range(1, i + 1):
        j1 = j1 + str(j) + ' '
    print(j1)

# v.2 While and For
i = 1
while i <= 5:
    j1 = ''
    for j in range(1, i + 1):
        j1 = j1 + str(j) + ' '
    print(j1)
    i += 1

# v.3 While Loop
i = 1
while i <= 6:
    j1 = ''
    j = 1
    while j < i:
        j1 = j1 + str(j) + ' '
        j += 1
    print(j1)
    i += 1

# v.4 Two loops - much loops. One Loop version
j = ''
for i in range(1, 6):
    j = j + str(i) + ' '
    print(j)

# v.5 One Loop
list_i = '1 2 3 4 5'
for i in range(0, 6):
    print(f"{list_i[0:i*2]}")
