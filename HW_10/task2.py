"""
2. (необов'язкове виконання) Створити програму, яка буде приймати число і
друкувати відповідне число в послідовності Фібоначчі, використовуючи рекурсію.
"""
def fibonacci(fib1, fib2, n):
    n = n - 1
    if n == 0: # showing the 1st number!
        return fib1
    fib3 = fib1 + fib2
    fib1 = fib2
    fib2 = fib3
    return fibonacci(fib1, fib2, n)

fib1 = 1
fib2 = 1
# idea with list for 2 number is too complicated for this task, IMHO

user_value = int(input("Write a whole number (no more than 997): "))
print(fibonacci(fib1, fib2, user_value))
