phonebook_dict = {
    "+11111111": "Tom",
    "+33333333": "Bob",
    "+55555555": "Alice",
    "+44444444v": "Tom"
}
key = "+55555555"
if key in phonebook_dict:
    user = phonebook_dict[key]
#    print(phonebook_dict)
else:
    print("Елемент не знайдено")

#print(phonebook_dict)
# stats: кількість записів
# show <name>: детальна інформація по імені

while True:
    print("Press key for continue: s - stats, a - add item, v - view items, n - name list, d - delete by name, x - exit")
    operation = input()
    match operation:
        case "s": # stats
            print(len(phonebook_dict))
        case "a": #  add item
            add_data_lst = input("Enter the the phone number and name separated by space: ").split()

            phonebook_dict[add_data_lst[0]] = add_data_lst[1]
            print("Add item complete")
        case "v": # view items
            for key, value in phonebook_dict.items():
                print(f"{value} have a phone number {key}")
        case "n": # name list
            for value in phonebook_dict.values():
                print(value)
        case "d": # delete by name
            add_data = input("Enter the name: ") #need name
            del phonebook_dict[add_data]
        case "x": # exit
            break
        case _:
            print("Select incorrect option. Try again:")
