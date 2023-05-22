class User:
    def __init__(self, name):
        self.name = name

    def __eq__(self, other):
        return other.name.upper() == self.name.upper():


first_user = User('OLEKSII')

second_user = User('Oleksii')

print(first_user.name)

print(second_user.name)

print(first_user == second_user)
