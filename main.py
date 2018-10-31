# some arifmetical operations
def func1(x=0, y=0):
    return x+y


def func2(x=0, y=0):
    if x >= y:
        return x-y
    else:
        return y-x


def func3(x=0, y=0):
    return x*y


x = 65
y = 48
print("sum: {}".format(func1(x, y)))
print("minus: {}".format(func2(y, x)))
print("multiplex: {}".format(func3(x, y)))
