class MyStr(str):

    def __str__(self):
        res = super().__str__()
        return res.upper()


my_str = MyStr('test')
print(my_str)
