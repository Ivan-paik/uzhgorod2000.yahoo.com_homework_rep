import json
from time import localtime, strftime

# # Make new .json with testing data. Run once.
# phonebook_dict = {
#     "+11111111": ["Tom", "Jones"],
#     "+33333333": ["Bob", "Marley"],
#     "+55555555": ["Alice", "Cooper"],
#     "+44444444": ["Tom", "Jones"],
#     "+77777777": ["Tom", "Cruise"],
#     "+88888888": ["Tom and Jerry", "Pets"],
#     "101":["q", "w"]
# }
#
# with open('phonebook_dict.json', "x") as phonebook:
#     json.dump(phonebook_dict, phonebook)


phonebook_dict = {}
json_string = {}

with open('phonebook_dict.json', "rt") as phonebook_json:
    phonebook_dict = json.load(phonebook_json)


# ===== Custom exception
class MyCustomException(Exception):
    def __init__(self, message, error_code):
        super().__init__(message)
        with open('my_custom_exeption.log', "a") as exeption_log_file:
            exeption_log_file.write(f"""{(message)} with code {error_code} excepted at {strftime("%H:%M:%S", localtime())}\n""")
        self.error_code = error_code

    def get_error_code(self):
        return self.error_code


# Decorator section
def definition_running_time(func):
    def wraper(*args):
        func(*args)
        with open('definition_running_time.log', "a") as definition_log_file:
            definition_log_file.write(f"""{func.__name__} run at {strftime("%H:%M:%S", localtime())}\n""")
    return wraper


# Definition section
@definition_running_time
def stats_command():
    print(f"Count of items: {len(phonebook_dict)}")
    return

@definition_running_time
def add_command(user_input):
    user_input_split = user_input.split()
    try:
        if user_input_split[0] in phonebook_dict:
            print("Same number is present. Can't add this item.")
            raise MyCustomException("Custom exception is occurred", 555)
            return None
        else:
            try:
                phonebook_dict[user_input_split[0]] = user_input_split[1], user_input_split[2]
            except IndexError:  # 3 text block needed (phone, first, last name). More - ok.
                print("All data needed. Please write it.")
            else:
                print("Add item complete.")
                with open('phonebook_dict.json', "w") as phonebook:
                    json.dump(phonebook_dict, phonebook)
            finally:
                   return None
    except MyCustomException as exc:
        print(f"{exc.get_error_code()}: {exc}")

@definition_running_time
def delete_command(delete_option, user_input):
    user_input_split = user_input.split()
    key_list_to_delete = []
    found_name = False

    if delete_option == '1': # delete by first name
        for key, value in phonebook_dict.items():
            if user_input_split[0] == value[0]:
                print(f"{value[0]} have a phone number {key}")
                key_list_to_delete.append(key)
                found_name = True

    if delete_option == '2': # delete by last name
        for key, value in phonebook_dict.items():
            if user_input_split[0] == value[1]:
                print(f"{value[1]} have a phone number {key}")
                key_list_to_delete.append(key)
                found_name = True

    if delete_option == '3': # delete by first + last name
        for key, value in phonebook_dict.items():
            if user_input_split[0] == value[0] and user_input_split[1] == value[1]:
                print(f"{value[0]} have a phone number {key}")
                key_list_to_delete.append(key)
                found_name = True

    if found_name:
        for key in key_list_to_delete:
            del phonebook_dict[key]
        print(f"'{user_input}' was deleted")
        with open('phonebook_dict.json', "w") as phonebook:
            json.dump(phonebook_dict, phonebook)
    else:
        print(f"'{user_input}' not found")

@definition_running_time
def list_command():
    for value in phonebook_dict.values():
        print(value)

@definition_running_time
def show_command(user_input):
    user_input_split = user_input.split()
    found_name = False
    for key, value in phonebook_dict.items():
        try:
            if user_input_split[0] == value[0] and user_input_split[1] == value[1]:
                print(f"'{user_input}' have a phone number {key}")
                found_name = True
        except IndexError:  # Only found first name
            print("First name was found, but it not enough. Specify the last name too.")
            return None

    if not found_name:
        print(f"'{user_input}' not found")
        return None


# Main program
while True:
    print("Print command name and press Enter: stats, add, delete, list, show, exit: ")
    operation = input()

    match operation:

        case "stats":
            stats_command()

        case "add":
            add_command(input("Write the the phone number, first and last name separated by space: "))

        case "delete": # delete by first name and/or last name
            delete_option = input("You want to delete by first name (1), by last name (2) or both (3). Write selected item:")
            delete_command(delete_option, input("Write first or/and last name separated by space than press Enter: "))

        case "list": # list of names
            list_command()

        case "show":
            show_command(input("Write the first and last name separated by space and press Enter: "))

        case "exit":
            break

        case _:
            print("Select incorrect option. Try again.")
