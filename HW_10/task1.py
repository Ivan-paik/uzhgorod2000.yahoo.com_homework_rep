"""
1. Написати рекурсію, яка буде друкувати числа від введенного користувачем до нуля.
Але ж це було в прикладах на уроці
"""
def countdown(n):
    print(n, end=" ")
    if n == 0:
        return
    return countdown(n-1)

user_value = input("Write a whole number (no more than 996): ")
countdown(int(user_value))
