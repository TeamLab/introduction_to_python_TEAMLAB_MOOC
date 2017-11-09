def asterisk_test(a, b, *args):
    return a+b+sum(args)


print(asterisk_test(1, 2, 3, 4, 5))


def asterisk_test_2(*args):
    x, y, z = args
    return x, y, z


print(asterisk_test_2(3, 4, 5))
