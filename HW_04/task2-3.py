input_text = input("Введіть тестові дані:")
if str.isdigit(input_text):
    if (int(input_text) % 2) == 0:
        print("Введенні дані є парним числом")
    else:
        print("Введенні дані є непарним числом")
elif str.isalpha(input_text):
    text_len = len(input_text)
    last_num_digit = int(str(text_len)[-1])
    if last_num_digit == 1:
        suffix = ''
    elif 1 < last_num_digit < 5:
        suffix = 'и'
    else:
        suffix = 'ів'
    print("Введенні дані містять тільки літери і є словом, довжиною", text_len, "символ" + suffix)
else:
    print("Введенні дані містять різні типи символів")