input_text = input("Введіть тестові дані:")
if str.isdigit(input_text):
    print("Введенні дані містять тільки цифри, тобто є цілим числом")
elif str.isalpha(input_text):
    print("Введенні дані містять тільки літери, тобто є словом")
else:
    print("Введенні дані містять різні типи символів")

# якщо набрана абракадабра, то може, коректніше, називати текстом, а не словом.