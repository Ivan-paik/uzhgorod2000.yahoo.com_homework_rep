a = 2
b = 5
c = 6

# v1
d = str(100 * a + 10 * b + c)
print(d)

# v2
a = str(a)
b = str(b)
c = str(c)
d = a + b + c
print(d)