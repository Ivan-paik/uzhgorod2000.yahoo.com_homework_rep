# Definition section
def sum_all_numbers(*numbers):
    result = 0
    for number in numbers:
        result += number
    return result

# Main program
#Ручний парсинг рядка для пошуку всіх чисел і тільки з тими функціями, які проходили
"""
Хотів обійтись без List, tuple. Все таки, одну нову функцію використав - exec (вибрав такий варіант 
обходу проблеми передачі вмісту рядкової змінної як аргументів в функцію).
Був ще варіант з генерацією змінних типу а1, а2 і тд. Їх потім збирав назад в строковий вид для 
передачі у функцію, але вийшло аж занадто громіздко, видалив щоб на позоритись.
"""
user_input = input('Please input numbers (integer, float, _E_ format) separated by space: ')
i = 1
temp_value = ''
for digit in user_input:
    if digit != " ":        # формуємо число, поки є символи "не пробіл"
        temp_value += digit
    else:                   # якщо є ще числа, будемо ліпити їх в рядок через кому.
        i += 1
        temp_value += ', '

exec('print(sum_all_numbers('+temp_value+'))')
