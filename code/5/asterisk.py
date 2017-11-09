def asterisk_test(a, b, *args):
    return a+b+sum(args)


print(asterisk_test(1, 2, 3, 4, 5))
