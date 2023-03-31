lst = ["qwe", "wEr", "erT", "rTY", "YuI"]

# v1. via definition
def in_upper(symbol):
    return symbol.upper()

upper_list = list(map(in_upper, lst))
print(upper_list)


# v2. via lambda func.
upper_list2 = list(map(lambda symbol: symbol.upper(), lst))
print(upper_list2)