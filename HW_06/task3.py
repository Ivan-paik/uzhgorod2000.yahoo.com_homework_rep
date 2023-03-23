"""
# Built-in function
"""
def max_volume1(*numbers):
    print(max(numbers))

max_volume1(1, 5, 3, 16, 4)

"""
# Create own function
"""
def bigger(a, b):
    if a > b:
        return a
    return b

def max_volume2(*numbers):
    i = True
    for number in numbers:
        if i :
            big_number = number
            i = False
        big_number = bigger(big_number, number)
    return big_number

print(max_volume2(1, 5, 3, 16, 4))

"""
# Create own function with lambda
"""
bigger2 = lambda a, b: a if a > b else b

def max_volume3(*numbers):
    i = True
    for number in numbers:
        if i :
            big_number = number
            i = False
        big_number = bigger2(number, big_number)

    return big_number

print(max_volume3(1, 5, 3, 16, 4))
