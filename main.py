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


def func4(x=0, y=0, z=0):
    return (x+y)*2-z


def func5():
    print("Only printing.")


x = 65
y = 48
z = 35
print("sum: {}".format(func1(x, y)))
print("minus: {}".format(func2(y, x)))
print("multiplex: {}".format(func3(x, y)))
print("function (x+y)*2 - z = {}".format(func4(x, y, z)))
func5()
print("zelen'")

s = 7
print("sum: {}".format(func1(x, s)))
print("minus: {}".format(func2(x, s)))

for i in range(8):
    print(i)
