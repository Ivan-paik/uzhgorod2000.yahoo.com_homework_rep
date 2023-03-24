input_text = input("Введіть тестові дані:")

match str.isdigit(input_text), str.isalpha(input_text):
    case  (True, False):
        if (int(input_text) % 2) == 0:
            print("Введенні дані є парним числом")
        else:
            print("Введенні дані є непарним числом")

    case (False, True):
            print("Введенні дані є словом")

    case _:
        print("Введенні дані містять різні типи символів")
