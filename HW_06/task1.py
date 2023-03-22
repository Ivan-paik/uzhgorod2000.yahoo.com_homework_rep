user_input = input('Input two number separated by space, please: ')

a = b = ''
number = 1

# Ручний парсинг рядка для пошуку обох чисел і тільки з тими функціями, які проходили.
for digit in user_input:
    if digit != " ":
        if number == 1 :
            a = a + digit
        else:
            b = b + digit
    else:
        number = 2

def Exponentiation (x, y):
    z = x ** y
    return(z)

print(f"{a} to the Power of {b} is {Exponentiation(int(a), int(b))}")
