# str, int, float, hex data
lst = ["abc", "44", "0", 3, 1.5, .2, "2.2", "44", 2e1, 0x11, "4*7"]

def digit_only(symbol):
    if type(symbol) == int or type(symbol) == float:
        return True
    else: # for str type only
        return(symbol.isdecimal())

digit_list = list(filter(digit_only, lst))
print(f"result: {digit_list}")
