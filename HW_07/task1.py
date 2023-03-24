# Testing data.
# Unique numbers. One man have a few phone numbers.
phonebook_dict = {
    "+11111111": "Tom",
    "+33333333": "Bob",
    "+55555555": "Alice",
    "+44444444": "Tom"
}

# Main program
while True:
    print("Print command name and press Enter: stats, add, delete, list, show, exit: ")
    operation = input()

    match operation:

        case "stats":
            print(f"Count of items: {len(phonebook_dict)}")

        case "add":
            user_input = input("Enter the the phone number and name separated by space: ").split()
            if user_input[0] in phonebook_dict:
                print("Same number is present. Can'n add this item")
            else:
                phonebook_dict[user_input[0]] = user_input[1]
                print("Add item complete")

        case "delete": # delete by name !!!
            user_input = input("Enter the name and press Enter: ")
            key_list_to_delete = []
            found_name = False
            for key, value in phonebook_dict.items():
                if user_input == value:
                    print(f"{value} have a phone number {key}")
                    key_list_to_delete.append(key)
                    found_name = True
            if found_name:
                for key in key_list_to_delete:
                    del phonebook_dict[key]
                print(f"'{user_input}' was deleted")
            else:
                print(f"'{user_input}' not found")

        case "list": # list of names
            for value in phonebook_dict.values():
                print(value)

        case "show":
            user_input = input("Enter the name and press Enter: ")

            found_name = False
            for key, value in phonebook_dict.items():
                if user_input == value:
                    print(f"{value} have a phone number {key}")
                    found_name = True
            if not found_name:
                print(f"'{user_input}' not found")

        case "exit":
            break

        case _:
            print("Select incorrect option. Try again:")
