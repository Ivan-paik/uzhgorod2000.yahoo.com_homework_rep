users = {
    "+11111111": "Tom",
    "+33333333": "Bob",
    "+55555555": "Alice"
}
key = "+55555555"
if key in users:
    user = users[key]
#    print(user)
else:
    print("Елемент не знайдено")

#print(users)

# stats: кількість записів

# Add user
users["+66666666"] = "Dennis"

#print(users)

# Del user by phone
del users["+66666666"]
#print(users)

# Show all values
#print(users.values())

# show <name>: детальна інформація по імені

while True:
    print("Press key for continue: A - add item, V - view items, N - viev name, D - delete by name, X - exit")
    operation = input()
    match operation:
        case "A":
            add_data_lst = input("Enter the the phone number and name separated by space: ").split()
            users[add_data_lst[0]] = add_data_lst[1]
            print("Add item complete")
        case "V":
            for key, value in users.items():
                print(f"{value} have a phone number {key}")
        case "N":
            for value in user.values():
             print(value)
        case "D":
            add_data = input("Enter the name: ")
            del users[add_data]
        case "X":
            break
        case _:
            print("Press correct option. Try again:")
