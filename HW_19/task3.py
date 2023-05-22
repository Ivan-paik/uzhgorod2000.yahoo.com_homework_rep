class MyStr(str):

    def __str__(self):
        return self.upper()


my_str = MyStr('test')
print(my_str)
