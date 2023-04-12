class TenEqualSigns:
    def __enter__(self):
        print("==========")

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type != None:
            print(f"Error {exc_type.__name__} was happend with {'key' + str(i)}")
        print("==========")
        return 1 #  something to return ???


my_dict = {"key1":"one", "key2":"two", "key4":"four"}


for i in range(1, 5):
    with TenEqualSigns():
        print(f"Program result is {my_dict['key' + str(i)]}")

print("End of program")