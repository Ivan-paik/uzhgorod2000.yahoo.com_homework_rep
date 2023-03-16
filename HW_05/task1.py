users_text = input('Print text here and press Enter:')
for letter in  users_text:
    if str.isupper(letter):
        print(f"'{letter}'- is a letter in upper case")
    elif str.islower(letter):
        print(f"'{letter}'- is a letter in lover case")
    elif str.isdigit(letter):
        if (int(letter) % 2) == 0:
            print(f"'{letter}'- is even digit")
        else:
            print(f"'{letter}'- is odd digit")
    else:
        print(f"'{letter}'- is symbol")
