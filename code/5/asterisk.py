def asterisk_test(a, b, *args):
    return a+b+sum(args)


print(asterisk_test(1, 2, 3, 4, 5))


def asterisk_test_2(*args):
    x, y, z = args
    return x, y, z


print(asterisk_test_2(3, 4, 5))


def kwargs_test_1(**kwargs):
    print(kwargs)

kwargs_test_1(first=3, second=4, third=5)


def kwargs_test_2(**kwargs):
    print(kwargs)
    print("First value is {first}".format(**kwargs))
    print("Second value is {second}".format(**kwargs))
    print("Third value is {third}".format(**kwargs))


kwargs_test_2(first=3, second=4, third=5)

def kwargs_test_3(one,two, *args, **kwargs):
    print(one+two+sum(args))
    print(kwargs)

kwargs_test_3(3,4,5,6,7,8,9, first=3, second=4, third=5)
