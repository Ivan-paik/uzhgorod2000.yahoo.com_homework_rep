"""
3. (необов'язкове виконання) Написати програму, яка буде повертати факторіал введеного числа, використовуючи рекурсію.
Але ж це було в прикладах на уроці
"""
def factorial(n: int) -> int :
    if n == 0:
        return 1
    return n * factorial(n - 1)

user_value = int(input("Write a whole number (no more than 998): "))
print(factorial(user_value))
