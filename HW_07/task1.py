users = {
    "+11111111": "Tom",
    "+33333333": "Bob",
    "+55555555": "Alice"
}
key = "+11111111"
if key in users:
    user = users[key]
    print(user)
else:
    print("Елемент не знайдено")

print(users)

# stats: кількість записів

# Add user
users["+66666666"] = "Dennis"

print(users)

# Del user by phone
del users["+66666666"]
print(users)

# Show all values
print(users.values())

# show <name>: детальна інформація по імені

while Thrue:

