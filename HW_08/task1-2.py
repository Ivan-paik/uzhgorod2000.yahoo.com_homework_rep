my_set1 = {1, 2, 3, 4}
my_set2 = {4, 3, 5, 6}

def equal_data(set1, set2):
    return set1.intersection(set2)

def unique_data(set1, set2):
    return set1.symmetric_difference(set2)

print(equal_data(my_set1, my_set2))

print(unique_data(my_set1, my_set2))
