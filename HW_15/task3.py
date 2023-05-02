import re

#==== Definitions
def convert_mails(text):
    result = re.findall(pattern, text)
    if result:
        for i in result:
            text = text.replace(i, i[0] + "***@***" + i[-1])
    return text

#===== Main program

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
    file = open(file_name,"r")
except FileNotFoundError:
    print("File not found")
else:
    file_name2 = "text_result.txt"
    file2=open(file_name2,"w")
    line=" "

    while line!="" :
        line=file.readline()
        str_new = convert_mails(line)
        file2.write(str_new)

    file.close
    file2.close
