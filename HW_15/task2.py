import re

""" creating the test file """
file_name = "text.txt"
file = open(file_name, "w")
file.write(""" "+11111111": ["Tom", "abcd@gmail.com"],
#  +33333333 0cde@gmail.com, - cdef@i.ua\n
defg@gmail.com, Tom:test1@gmail.com,
"pet"-"ghij@gmail.com",hijk@gmail.com.ua  
qwery@yahoo.com - unknown address
te1@gmail.com,te2@gmail.com,te3@gmail.com
\n""")
file.close()

pattern = '[A-Za-z0-9._-]*@[A-Za-z0-9.]*'  # we accept that all addresses are entered correctly

file_name = input("enter file name (text.txt): ")

try:
    file = open(file_name)
except FileNotFoundError:
    print("File not found")

else:
    with open(file_name) as file:
        lines = [re.sub(pattern, '*@*', line) for line in file]
    with open(file_name, 'w') as file:
        file.writelines(lines)
