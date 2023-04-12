from time import localtime, strftime


def func_name_and_time_decorator(times: int):
    # print(times)
    def wraper(func):
        def inner(*args, **kwargs):
            for i in range(times):
                print(f"""{func.__name__} run at {strftime("%H:%M:%S", localtime())}""")
            return func(*args, **kwargs)
        return inner
    return wraper

times = 3

@func_name_and_time_decorator(times)
def my_func1(*args, **kwargs):
    print(f"{args},{kwargs}")
    return None

my_func1(1, "one", param1=0, param2="null")


@func_name_and_time_decorator(times)
def my_func2(*args, **kwargs):
    print(f"{args},{kwargs}")
    return None

my_func2(1, "one")


@func_name_and_time_decorator(times)
def my_func3(*args, **kwargs):
    print(f"{args},{kwargs}")
    return None

my_func3(param1=0, param2="null")
