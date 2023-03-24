user_input = input('Input two numbers separated by space, please: ')

a = b = ''
number = 1

# Ручний парсинг рядка для пошуку обох чисел і тільки з тими функціями, які проходили.
for digit in user_input:
    if digit != " ": # просто шукаєм пробіл після числа, бо це розділювач
        if number == 1 : # формуємо перше число
            a = a + digit
        else:
            b = b + digit # формуємо друге число
    else:
        number = 2

def exponentiation(x, y):
    z = x ** y
    return(z)

print(f"{a} to the Power of {b} is {Exponentiation(int(a), int(b))}")
