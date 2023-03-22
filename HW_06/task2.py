def sum_all_numbers(*numbers):
    result = 0
    for number in numbers:
        result = result + number
    return result

a = sum_all_numbers(1, 3, 5)
print(a)