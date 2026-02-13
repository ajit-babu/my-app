# This file has intentional code quality issues

def unused_function():
    pass


def function_with_too_many_params(a, b, c, d, e, f, g):
    x = 1
    y = 2
    z = 3  # unused variable
    return a + b + c + d + e + f + g


# Duplicate code
def duplicate1():
    print("test")
    print("test")
    print("test")


def duplicate2():
    print("test")
    print("test")
    print("test")
