from time import localtime, strftime


def func_name_and_time_decorator(func):
    def wraper(*args, **kwargs):
        func(args, kwargs)
        print(f"""{func.__name__} run at {strftime("%H:%M:%S", localtime())}""")
    return wraper


@func_name_and_time_decorator
def my_func1(*args, **kwargs):
    print(f"{args}")  # don't undestand why only args enough?
    return None

my_func1(1, "one", param1=0, param2="null")


@func_name_and_time_decorator
def my_func2(*args, **kwargs):
    print(f"{args}")
    return None

my_func2(1, "one")


@func_name_and_time_decorator
def my_func3(*args, **kwargs):
    print(f"{args}")
    return None

my_func3(param1=0, param2="null")
